# Generated by Django 2.1.5 on 2019-01-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190130_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='car_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='license',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
