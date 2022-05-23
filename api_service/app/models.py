from sqlalchemy import Column, desc, Float, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from api_service.app.database import Base


class Currency(Base):
    __tablename__ = "currency"

    id = Column(String, primary_key=True, index=True)
    valute_id = Column(String)
    num_code = Column(Integer)
    char_code = Column(String)
    name = Column(String, unique=True)

    records = relationship("Record", back_populates="currency")

    def __repr__(self):
        return (
            f"{self.__class__.__name__} {self.char_code}"
        )


class Record(Base):
    __tablename__ = "records"

    id = Column(String, primary_key=True, index=True)
    nominal = Column(Integer)
    value = Column(Float, index=True)
    currency_id = Column(String, ForeignKey("currency.id"))
    timestamp = Column(TIMESTAMP)

    currency = relationship("Currency", back_populates="records")

    def __repr__(self):
        return (
            f"{self.__class__.__name__} {self.id}"
        )

    @classmethod
    async def get_last_rate(cls, session: AsyncSession, char_code: str):
        query = select(cls).join(cls.currency).filter(Currency.char_code == char_code).order_by(desc(cls.timestamp))
        objects = await session.execute(query)
        try:
            (model_object,) = objects.first()
        except TypeError:
            return "Not found"
        return model_object.value
