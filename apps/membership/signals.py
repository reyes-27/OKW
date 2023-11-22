from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# from .models import Customer, CustomUser
from .models import CustomerMembership


@receiver(pre_save, sender=CustomerMembership)
def set_end_date(sender, instance, **kwargs): 
    if instance.membership.duration:
        instance.end_date = instance.start_date + instance.membership.duration