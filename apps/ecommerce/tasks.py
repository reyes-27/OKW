from celery import shared_task

@shared_task
def greet():
    return "You are my sunshine"