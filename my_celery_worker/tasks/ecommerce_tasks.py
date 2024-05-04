from celery import shared_task

@shared_task
def split_numbers(x, y):
    return x / y