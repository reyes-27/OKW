# Generated by Django 4.2.7 on 2023-11-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_alter_membership_duration_alter_membership_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermembership',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]