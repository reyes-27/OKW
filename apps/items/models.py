from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from django_resized import ResizedImageField
from django.db.models import Sum, F
import uuid
from django.utils.text import slugify
# Create your models here.

class AbstractItem(models.Model):
    id =                models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unit_price =        models.FloatField()
    discount =          models.FloatField(default=0.00, blank=True, null=True)
    final_price =       models.FloatField()
    class Meta:
        abstract = True


class Product(AbstractItem):
#STOCK VALUE AUTOMATICALLY DECREASES ONCE A CUSTOMER'S ORDER STATE IS SET TO TRUE
    slug = models.SlugField(editable=False, blank=True)
    name = models.CharField(max_length=50)
    description = RichTextField()
    stock = models.PositiveIntegerField()
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    
    def __str__(self) -> str:
        return self.slug

    # def get_final_price(self):
    #     if self.discount:
    #         return Product.objects.filter(id=self.id).annotate(self.unit_price - self.discount).values()
    def save(self, *args, **kwargs):
        if not self.final_price:
            self.final_price = self.unit_price
        if self.discount > 0:
            self.final_price =self.unit_price - self.unit_price * self.discount
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

def image_path(instance, filename):
    return f'images/products/{instance.product.slug}/{filename}'
class ProductImage(models.Model):
    image = ResizedImageField(upload_to=image_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image_set")
    level = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    def __str__(self):
        return f"{self.product.name} <-> {self.image.name.split("/")[-1]}({self.level})"
    class Meta:
        ordering = ["level"]