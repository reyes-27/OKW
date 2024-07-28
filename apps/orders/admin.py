from django.contrib import admin
from .models import (
    Order,
    CartItem,
    Cart,
    Payment,
)
# Register your models here.
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payment)