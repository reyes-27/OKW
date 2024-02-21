from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_countries.fields import CountryField 
import uuid
from apps.membership.models import CustomerMembership
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        email=self.normalize_email(email)
        user=self.model(email=email, username=username)
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user=self.create_user(email=email, username=username, password=password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField()
    objects = CustomUserManager()

#GOTTA MOVE THIS TO ECOMMERCE APP


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_customer")
    phone = models.CharField(max_length=30)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    country = CountryField()
    membership = models.OneToOneField(to=CustomerMembership, on_delete=models.CASCADE, related_name="customer", blank=True)
    reputation = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=0, editable=False)
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        # if self.membership != None:
        #     self.membership = CustomerMembership.default_object
        super(Customer, self).save(*args, **kwargs)