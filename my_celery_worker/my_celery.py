import os
from celery import Celery
# from ..core.settings import BASE_DIR

# env = Env()
# env.read_env(os.path.join(BASE_DIR,'../core/.env'))

app = Celery("tasks",
            # broker="redis://redis:6379/0",
            # backend="redis://redis:6379/0",
            include=[
                'tasks.ecommerce_tasks',
                    ],
            )
app.config_from_object('celery_settings')
app.conf.update(
    result_expires=3600,
)

app.autodiscover_tasks()

app.task()
if __name__ == '__main__':
    app.start()