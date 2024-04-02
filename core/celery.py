import os
from celery import Celery
from environ import Env
from .settings import BASE_DIR

env = Env()
env.read_env(os.path.join(BASE_DIR,'core/.env'))

# env.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery("core")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()