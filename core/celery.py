import os
from celery import Celery
from environ import Env
from .settings import BASE_DIR

env = Env()
env.read_env(os.path.join(BASE_DIR,'core/.env'))

# env.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery(
    "core",
    include=[
        "apps.ecommerce.tasks"
    ]
    )

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.task_routes = {
#     'apps.ecommerce.add': {
#         'queue':'queue'
#     },
#     'apps.ecommerce.subtract': {
#         'queue':'queue1'
#     }
# }

# app.conf.broker_transport_options = {
#     "priority_steps":list(range(10)),
#     "sep":':',
#     "query_order_strategy":"priority"

# }

app.autodiscover_tasks()