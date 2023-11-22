from django.db import models
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from apps.items.models import AbstractItem
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
import uuid
# Create your models here.

class Membership(AbstractItem):
    slug = models.SlugField(blank=True, editable=False)
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(validators=[MaxValueValidator(3)], unique=True)
    desc = models.TextField()
    duration = models.DurationField(blank=True, null=True)
    @classmethod
    def default_object(cls):
        obj, created = cls.objects.get_or_create(level=0, defaults={
            'name':'Standard',
            'desc':'This is the most basic membership, gives you authorization to interact with posts and buy stuff',
            'unit_price':0.00,
            'discount':0,
        }) 
        return obj
    
    def __str__(self):
        return f'{self.name} - {self.level}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Membership, self).save(*args, **kwargs)
    
class CustomerMembership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, default=Membership.default_object)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        txt = f'{self.membership.name} -- {self.membership.level}'
        return txt
    

    # def save(self, *args, **kwargs):
    #     if self.membership.duration:
    #         self.end_date = self.start_date + self.membership.duration
    #     super(CustomerMembership, self).save(*args, **kwargs)

