import os

from celery import Celery

REQUEST_FREQUENCY = os.getenv("REQUEST_FREQUENCY", 30.0)

app = Celery("Celery", include=["tasks_service.app_code.tasks"])

app.config_from_object("tasks_service.app_code.celery_config")

app.conf.beat_schedule = {
    "periodic_request_central_bank": {
        "task": "tasks_service.app_code.tasks.request_central_bank",
        "schedule": REQUEST_FREQUENCY
    }
}
