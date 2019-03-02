# Generated by Django 2.1.5 on 2019-02-02 01:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, null=True)),
                ('arrival', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('num_pass', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('CanShare', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('open', 'open'), ('confirmed', 'confirmed'), ('completed', 'completed')], default='null', max_length=255)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ride_driver', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ride_owner', to=settings.AUTH_USER_MODEL)),
                ('sharer', models.ManyToManyField(blank=True, null=True, related_name='ride_sharer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='rorequest',
            name='username',
        ),
        migrations.DeleteModel(
            name='RORequest',
        ),
    ]
