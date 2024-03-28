from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django_countries.fields import CountryField 
from django_resized import ResizedImageField
from .utils import image_path
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
    id =            models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email =         models.EmailField()
    objects =       CustomUserManager()
    # class Meta:
    #     verbose_name="custom_user"

class Customer(models.Model):
    id =                    models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user =                  models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="customer")
    phone =                 models.CharField(max_length=30)
    first_name =            models.CharField(max_length=40)
    last_name =             models.CharField(max_length=40)
    country =               CountryField()
    profile_pic =           ResizedImageField(upload_to=image_path, default="default.png")
    reputation =            models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=0, editable=False)
    is_seller =             models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} Customer'
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        # if self.membership != None:
        #     self.membership = CustomerMembership.default_object
        super(Customer, self).save(*args, **kwargs)


