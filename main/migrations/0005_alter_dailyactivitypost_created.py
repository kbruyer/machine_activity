# Generated by Django 4.0.6 on 2022-07-28 04:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_dailyactivitypost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyactivitypost',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 7, 28, 4, 49, 30, 315668, tzinfo=utc)),
        ),
    ]
