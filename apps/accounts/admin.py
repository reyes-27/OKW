from django.contrib import admin
from .models import Customer, CustomUser
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomUser)