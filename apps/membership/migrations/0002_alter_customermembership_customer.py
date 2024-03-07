# Generated by Django 4.2.7 on 2024-03-02 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermembership',
            name='customer',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL),
        ),
    ]