from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# from .models import Customer, CustomUser
from .models import CustomerMembership
from django.utils import timezone

@receiver(post_save, sender=CustomerMembership)
def set_end_date(sender, created, instance, *args, **kwargs):
    if instance.sample.duration:
        if not instance.end_date:
            instance.end_date = instance.start_date + instance.sample.duration
            instance.save()

