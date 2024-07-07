from django.db import models
from django.db.models import (
    F,
    Sum,
    )
from apps.accounts.models import Customer
from apps.items.models import Product
from uuid import uuid4

# Create your models here.

class Payment(models.Model):
    payment_id =            models.PositiveBigIntegerField()
    payment_status =        models.BooleanField(default=False)
    total =                 models.FloatField(default=0)
    created_at =            models.DateTimeField(auto_now_add=True)
    modified_at =           models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total = self.order.get_total()
        super(Payment, self).save(*args, **kwargs)



class Order(models.Model):
    status_choices = (
        ("SHIPPED", "Shipped"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELED", "Canceled"),
        ("P_SHIPPED", "Partially shipped"),
        ("OTHER", "Not confirmed"),
    )
    
    id =                    models.UUIDField(primary_key=True, editable=False, default=uuid4)
    customer =              models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart =                  models.OneToOneField("Cart", on_delete=models.SET_NULL, blank=True, null=True)
    payment =               models.OneToOneField(Payment, blank=True, null=True, on_delete=models.SET_NULL)
    status =                models.CharField(max_length=155, choices=status_choices, default="OTHER")
    created_at =            models.DateTimeField(auto_now_add=True)
    modified_at =           models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.order_total = self.cart.cart_total
        super().save(*args, **kwargs)

    def get_total(self, *args, **kwargs):
        """Whenever you submit an order, this function is called and it annotates an order_total value to the order instance"""
        total_obj = Order.objects.filter(pk=self.pk).annotate(order_total = Sum(F("items__item_total")))
        return total_obj

    def __str__(self):
        return f"{self.customer.full_name} : ({self.created_at.date().strftime('%d/%m/%Y')})"

class CartItem(models.Model):
    id =                    models.UUIDField(primary_key=True, editable=False, default=uuid4)
    product =               models.ForeignKey(Product, on_delete=models.CASCADE)
    cart =                  models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="items")
    quantity =              models.IntegerField()
    item_total =            models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if self.quantity > self.product.stock:
            raise Exception("You can't order more items than are left")
        else:
            self.item_total = self.product.final_price * self.quantity
            super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'
    
class Cart(models.Model):
    id =                    models.UUIDField(primary_key=True, default=uuid4, editable=False)
    customer =              models.OneToOneField(Customer, on_delete=models.CASCADE)
    cart_total =            models.FloatField(default=0)
    created_at =            models.DateTimeField(auto_now_add=True)
    # create a list of all values iterating over self.items.all(), append the item.total_price
    def save(self, *args, **kwargs):
        super(Cart, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.customer.user.username}'s cart"
    
    def get_cart_total(self):
        return Cart.objects.filter(customer=self.customer).annotate(cart_total=Sum(F("items__product_price")))
# A CART WILL HANDLE MULTIPLE ORDERS 
            
#summarize Order.total : Sum() 
            
# if paid == True when saving an order object, product's stock is going to decrese by the quantity of that OrderItem, and get_total method is called
    
#order.order_items.product.stock()