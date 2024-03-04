from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# from .models import Customer, CustomUser
from .models import CustomerMembership
from django.utils import timezone

@receiver(post_save, sender=CustomerMembership)
def set_end_date(sender, created, instance, *args, **kwargs):
    if created:
        if instance.sample.duration:
            # instance.start_date = timezone.now().date()
            instance.end_date = instance.start_date + instance.model.duration
            instance.save()
    # print(instance.start_date, "------------>", instance.end_date, " : ", instance.model)

