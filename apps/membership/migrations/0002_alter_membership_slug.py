# Generated by Django 4.2.7 on 2023-11-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
