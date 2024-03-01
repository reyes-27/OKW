# Generated by Django 4.2.7 on 2023-11-16 16:44

import apps.items.models
import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.FloatField(blank=True, default=0.0, null=True)),
                ('name', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('stock', models.PositiveIntegerField()),
                ('rate', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, scale=1, size=[1920, 1080], upload_to=apps.items.models.image_path)),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'ordering': ['level'],
            },
        ),
    ]
