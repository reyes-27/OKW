from django.db import models

# Create your models here.

class Category(models.Model):
    parent =                models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    name =                  models.CharField(max_length=155)
    desc =                  models.TextField()
    class Meta:
        verbose_name_plural = 'Categories'