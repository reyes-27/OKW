from django.db import models
from apps.accounts.models import Customer
from apps.items.models import Product

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total =         models.DecimalField(max_digits=6, decimal_places=2)
    payment_id =    models.PositiveBigIntegerField()
    created_at =    models.DateTimeField(auto_now_add=True)
    modified_at =   models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if self.quantity > self.product.stock:
            raise Exception("You can't order more items than are left")
        else:
            super(OrderItem, self).super(*args, **kwargs)

# A CART WILL HANDLE MULTIPLE ORDERS 