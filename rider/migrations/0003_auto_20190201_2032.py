# Generated by Django 2.1.5 on 2019-02-02 01:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rider', '0002_auto_20190201_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='num_pass',
            field=models.PositiveIntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
