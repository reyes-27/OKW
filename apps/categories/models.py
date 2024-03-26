from django.db import models

# Create your models here.

class Category(models.Model):
    parent =                models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name="children")
    name =                  models.CharField(max_length=155)
    desc =                  models.TextField()

    def save(self, *args, **kwargs):
        if self.parent == self:
            raise Exception("Parent attr and current instance can't be the same object.")
        else:
            super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

