from django.contrib import admin
from .models import (
    Membership,
    CustomerMembership,
    )
# Register your models here.

admin.site.register(Membership)
admin.site.register(CustomerMembership)