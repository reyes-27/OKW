from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from django_resized import ResizedImageField
from django.db.models import Sum, F
import uuid
# Create your models here.
class AbstractItem(models.Model):
    id =                models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    unit_price =             models.DecimalField(max_digits=5, decimal_places=2)
    discount =          models.FloatField(default=0.00, blank=True, null=True)
    class Meta:
        abstract = True


class Product(AbstractItem):
#STOCK VALUE AUTOMATICALLY DECREASES ONCE A CUSTOMER'S ORDER STATE IS SET TO TRUE
    name = models.CharField(max_length=50)
    description = RichTextField()
    stock = models.PositiveIntegerField()
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    
    def get_final_price(self):
        return Product.objects.filter(id=self.id).annotate(self.unit_price * self.discount).values()


def cover_path(instance, filename):
    return f'/images/products/{instance}/{filename}'
class ProductCover(models.Model):
    image = ResizedImageField(upload_to=cover_path)
    level = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    class Meta:
        ordering = ["level"]