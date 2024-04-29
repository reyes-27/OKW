from celery import shared_task

@shared_task(
        name="sum-of-numbers",
        # bind=True,
        # acks_late=True,
        )
def add(x, y, queue="queue:0"):
    return x + y