import os
from celery import Celery
# from ..core.settings import BASE_DIR

# env = Env()
# env.read_env(os.path.join(BASE_DIR,'../core/.env'))

app = Celery("tasks")
app.config_from_object('my_celery_config')
# app.conf.broker_url = 'redis://redis:6379/0'
# app.conf.result_backend = 'redis://redis:6379/0'
# app.autodiscover_tasks()