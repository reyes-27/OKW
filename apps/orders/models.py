from django.db import models
from django.db.models import (
    F,
    Sum,
    )
from apps.ecommerce.models import Customer
from apps.items.models import Product
from uuid import uuid4

# Create your models here.

class Order(models.Model):
    id =                    models.UUIDField(primary_key=True, editable=False, default=uuid4)
    payment_id =            models.PositiveBigIntegerField()
    customer =              models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_status =        models.BooleanField(default=False)
    date_ordered =          models.DateTimeField(auto_now_add=True)
    order_total =           models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_at =            models.DateTimeField(auto_now_add=True)
    modified_at =           models.DateTimeField(auto_now=True)

    def get_total(self, *args, **kwargs) -> object:
        """Whenever you submit an order, this function is called and it annotates an order_total value to the order instance"""
        total_obj = Order.objects.filter(pk=self.pk).annotate(order_total = Sum(F("items__item_total")))
        return total_obj

    def __str__(self):
        return f"{self.customer.get_fullname()} : ({self.date_ordered.date().strftime('%d/%m/%Y')})"

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()
    item_total = models.PositiveIntegerField(default=0)



    def save(self, *args, **kwargs):
        if self.quantity > self.product.stock:
            raise Exception("You can't order more items than are left")
        else:
            self.item_total = self.product.unit_price * self.quantity
            super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'
# A CART WILL HANDLE MULTIPLE ORDERS 
            
#summarize Order.total : Sum() 
            
# if paid == True when saving an order object, product's stock is going to decrese by the quantity of that OrderItem, and get_total method is called
    
#order.order_items.product.stock()