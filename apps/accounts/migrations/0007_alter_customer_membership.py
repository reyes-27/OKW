# Generated by Django 4.2.7 on 2023-12-10 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_alter_customermembership_status'),
        ('accounts', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='membership',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='membership.customermembership'),
        ),
    ]
