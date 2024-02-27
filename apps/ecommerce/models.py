from django.db import models
from django_resized import ResizedImageField
from apps.orders.models import OrderItem
from uuid import uuid4
from django.db.models import Sum, F
from apps.accounts.models import CustomUser
from apps.membership.models import CustomerMembership
from django.core.validators import MaxValueValidator
from django_countries.fields import CountryField 


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_customer")
    phone = models.CharField(max_length=30)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    country = CountryField()
    membership = models.OneToOneField(to=CustomerMembership, on_delete=models.CASCADE, related_name="customer", blank=True)
    reputation = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=0, editable=False)
    is_seller = models.BooleanField(default=False)
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        # if self.membership != None:
        #     self.membership = CustomerMembership.default_object
        super(Customer, self).save(*args, **kwargs)


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

        