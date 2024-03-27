from django.db.models.signals import (
    pre_save,
    post_save,
    )
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CustomUser
from apps.membership.models import CustomerMembership

@receiver(post_save, sender=CustomUser)
def set_membership(sender, created, instance, *args, **kwargs):
    if created:
        CustomerMembership.default_object(user=instance)
