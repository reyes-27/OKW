from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save
from .models import (
    Cart,
    Order,
    Payment
    )
from apps.items.models import Product

# @receiver(post_save, sender=OrderItem)
# def update_order_total(sender, instance, *args, **kwargs):
#         instance.order.total = 


# #update Order's total whenever an OrderItem instance is saved 

@receiver(signal=post_save, sender=Order)
def check_order(sender, instance, *args, **kwargs):
    """This signal calls discount stock method"""
    if instance.status == 'CONFIRMED':

        for item in instance.cart.items.all():
            product = Product.objects.get(id=item.product.id)
            product.stock -= item.quantity
            product.save()

@receiver(signal=post_save, sender=Payment)
def confirm_order(sender, instance, *args, **kwargs):
    if instance.payment_status:
        instance.order.status = 'CONFIRMED'
        instance.order.save()