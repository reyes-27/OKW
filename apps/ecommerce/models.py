from django.db import models
from django_resized import ResizedImageField
from apps.orders.models import OrderItem
from apps.accounts.models import Customer
from uuid import uuid4
from django.db.models import Sum, F

# Create your models here.

def demo_loc(instance, filename):
    return f'demo/{instance}/{filename}'

class Clothes(models.Model):
    name = models.CharField(max_length=50)
    demo = ResizedImageField(upload_to=demo_loc)

    class Meta:
        verbose_name_plural="Clothes"

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return f"{self.customer.user.username}'s cart"
    def get_cart_total(self):
        return Cart.objects.filter(customer=self.customer).annotate(cart_total=Sum(F("items__")))
    
# class Article(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    # slug = models.SlugField()

        