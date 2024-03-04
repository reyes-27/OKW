from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from django_resized import ResizedImageField
from django.db.models import Sum, F
import uuid
from django.utils.text import slugify
from apps.categories.models import Category
from apps.accounts.models import Customer

# Create your models here.

class AbstractItem(models.Model):
    id =                models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unit_price =        models.FloatField()
    discount =          models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)], blank=True, default=0)
    final_price =       models.FloatField(blank=True)
    class Meta:
        abstract = True


class Product(AbstractItem):
    slug =              models.SlugField(editable=False)
    seller =            models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="products")
    name =              models.CharField(max_length=50)
    description =       RichTextField()
    stock =             models.PositiveIntegerField()
    rate =              models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=0)
    category =          models.ManyToManyField(Category)
    
    def __str__(self) -> str:
        return self.slug

    def save(self, *args, **kwargs):
        if not self.seller.is_seller:
            raise Exception(f"{self.seller} is not allowed to sell products. Customer object must have the seller property set to True")
        if not self.final_price:
            if self.unit_price >= 0:
                self.final_price = self.unit_price
            else:
                self.final_price = 0
        if self.discount > 0:
            self.final_price = round(self.unit_price - self.unit_price * (self.discount / 100), 2)
        self.slug = slugify(f"{self.name}_{str(self.id).split("-")[1]}")
        super(Product, self).save(*args, **kwargs)

def image_path(instance, filename):
    return f'images/products/{instance.product.slug}/{filename}'
class ProductImage(models.Model):
    image =             ResizedImageField(upload_to=image_path)
    product =           models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image_set")
    level =             models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    def __str__(self):
        return f"{self.product.name} <-> {self.image.name.split("/")[-1]}({self.level})"
    class Meta:
        ordering = ["level"]