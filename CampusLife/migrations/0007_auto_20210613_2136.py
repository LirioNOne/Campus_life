# Generated by Django 3.2.4 on 2021-06-13 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CampusLife', '0006_auto_20210610_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='going_to_event',
            field=models.ManyToManyField(blank=True, default=None, related_name='event_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Иду', 'Иду'), ('Не иду', 'Не иду')], default='Иду', max_length=10),
        ),
    ]
