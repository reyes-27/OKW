from django.db import models
from apps.orders.models import Order
# Create your models here.

class Invoice(models.Model):
    order =         models.ForeignKey(Order, related_name="invoices", null=True, blank=True, on_delete=models.CASCADE)
    comment =       models.TextField()
