# Generated by Django 4.0.6 on 2022-08-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_dailyactivitypost_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyactivitypost',
            name='description',
            field=models.TextField(max_length=1500, null=True),
        ),
    ]
