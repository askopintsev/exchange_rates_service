from celery import Task

from tasks_service.app_code.celery_app import app
from tasks_service.app_code.handlers import get_and_save_cb_data
from tasks_service.app_code.database import db_session


class SqlAlchemyTask(Task):
    """An abstract Celery Task that ensures that the connection the the
    database is closed on task completion"""
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        db_session.remove()


@app.task(base=SqlAlchemyTask, max_retries=5, default_retry_delay=60)
def request_central_bank():
    """
    Celery task for data parsing from Central Bank API.
    """
    get_and_save_cb_data()
