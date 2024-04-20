from celery import shared_task
import time

@shared_task
def subtract(x, y, queue="queue"):
    time.sleep(3)
    return x - y

@shared_task
def add(x, y, queue="queue:1"):
    time.sleep(3)
    return x + y