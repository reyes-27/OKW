from django.db import models
import uuid
from apps.ecommerce.models import (
    Clothes,
    )
from apps.accounts.models import Customer
# Create your models here.

def sp_loc(instance, filename):
    return f'sp/{instance}/{filename}'

#I'd better make a model for clothes with examples

class SpecialOrder(models.Model):
    material_choices = (
        ("PL", "polyester"),
        ("CT", "cotton"),
    )
    # clothes_choices = (
    #     ("LSS", "Long sleeve shirt"),
    #     ("VTS", "v-neck t-shirt"),
    #     ()
    # )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="special_orders")
    sketch = models.ImageField(upload_to=sp_loc, blank=True, null=True)
    text = models.TextField(help_text="<p>Here you gotta specify your ideas</p>")
    material = models.CharField(max_length=100, choices=material_choices)
    # type_of_clothes = models.CharField(max_length=100, choices=clothes_choices)
    type_of_clothes = models.ManyToManyField(Clothes)
    