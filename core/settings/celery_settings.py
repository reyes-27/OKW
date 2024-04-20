CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_TASK_ROUTES = {
    'apps.ecommerce.add': {
        'queue':'queue:1'
    },
    'apps.ecommerce.subtract': {
        'queue':'queue'
    },
}
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "priority_steps":list(range(10)),
    "sep":':',
    "query_order_strategy":"priority",
}