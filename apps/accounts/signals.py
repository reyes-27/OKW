from django.db.models.signals import (
    pre_save,
    post_save,
    )
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Customer, CustomUser



# @receiver(pre_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         new_profile=Customer.objects.create(user=instance)
#     instance.user_profile.save()

# @receiver(user_logged_in)
# def check_membership_status(sender, request, user, **kwargs):
#     if user.user_customer and user.user_customer.membership:
#         user.user_customer.membership.set_status()
