from django.db import models
from django_resized import ResizedImageField



# Create your models here.

def demo_loc(instance, filename):
    return f'demo/{instance}/{filename}'

class Clothes(models.Model):
    name = models.CharField(max_length=50)
    demo = ResizedImageField(upload_to=demo_loc)

    class Meta:
        verbose_name_plural="Clothes"



        