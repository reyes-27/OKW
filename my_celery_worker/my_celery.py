import os
from celery import Celery

app = Celery("tasks",
            include=[
                'tasks.ecommerce_tasks',
                    ],
            )
app.config_from_object('celery_settings')
app.conf.task_routes = {
    'tasks.ecommerce_tasks.split_numbers': {
        'queue':'queue:4'
    }
}

app.autodiscover_tasks()

# app.task()
if __name__ == '__main__':
    app.start()