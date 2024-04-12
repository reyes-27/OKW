import os
from celery import Celery
# from ..core.settings import BASE_DIR

# env = Env()
# env.read_env(os.path.join(BASE_DIR,'../core/.env'))

app = Celery("tasks")
app.config_from_object('my_celery_config')

# app.autodiscover_tasks()