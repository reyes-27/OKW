# Generated by Django 4.2.7 on 2023-11-25 16:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_alter_customermembership_end_date'),
        ('accounts', '0003_alter_customer_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='membership',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='membership.customermembership'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='reputation',
            field=models.PositiveIntegerField(default=0, editable=False, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
