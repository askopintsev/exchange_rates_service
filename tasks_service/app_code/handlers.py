import datetime
import os
from uuid import uuid4

from lxml import objectify
import requests

from api_service.app.models import Currency, Record

from tasks_service.app_code.database import db_session

ALLOWED_VALUTES = os.getenv("ALLOWED_VALUTES", ['CNY', 'EUR', 'USD'])
CB_URL = os.getenv("CB_URL", "https://www.cbr.ru/scripts/XML_daily.asp")


def get_and_save_cb_data():
    """
    Performs parsing and saving of data from Central Bank to Database.
    :return: None
    """

    response = requests.get(CB_URL)
    data_root = objectify.fromstring(response.content)

    objects_to_create = []
    for valute in list(data_root.Valute):
        if valute.CharCode in ALLOWED_VALUTES:
            currency_object = db_session.query(Currency).filter(Currency.char_code == str(valute.CharCode)).first()

            if not currency_object:
                currency_object = Currency(
                    id=uuid4(),
                    valute_id=str(valute.attrib.get('ID')),
                    num_code=int(valute.NumCode),
                    char_code=str(valute.CharCode),
                    name=str(valute.Name),
                )
                objects_to_create.append(currency_object)

            new_record = Record(
                id=uuid4(),
                currency_id=currency_object.id,
                nominal=int(valute.Nominal),
                value=float(str(valute.Value).replace(',', '.')),
                timestamp=datetime.datetime.now(),
            )
            objects_to_create.append(new_record)

    db_session.bulk_save_objects(objects_to_create)
    db_session.commit()
