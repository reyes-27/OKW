# Generated by Django 4.2.7 on 2024-03-05 15:21

import apps.accounts.utils
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.png', force_format='JPEG', keep_meta=True, quality=100, scale=1, size=[1920, 1080], upload_to=apps.accounts.utils.image_path),
        ),
    ]