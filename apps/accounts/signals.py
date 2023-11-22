from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Customer, CustomUser


# @receiver(pre_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         new_profile=Customer.objects.create(user=instance)
#     instance.user_profile.save()
