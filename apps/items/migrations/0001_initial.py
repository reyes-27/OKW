# Generated by Django 4.2.7 on 2024-03-21 22:45

import apps.items.models
import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('unit_price', models.FloatField()),
                ('discount', models.PositiveSmallIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(100)])),
                ('final_price', models.FloatField(blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('name', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('stock', models.PositiveIntegerField()),
                ('rate', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
                ('categories', models.ManyToManyField(to='categories.category')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='accounts.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, scale=1, size=[1920, 1080], upload_to=apps.items.models.image_path)),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_set', to='items.product')),
            ],
            options={
                'ordering': ['level'],
            },
        ),
    ]
