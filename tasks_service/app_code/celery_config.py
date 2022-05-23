import os


broker_url = os.getenv("BROKER_URL", "amqp://guest:guest@rabbitmq:5672")
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Europe/Moscow"
enable_utc = True
