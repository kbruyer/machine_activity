# Generated by Django 4.0.6 on 2022-08-14 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_incident_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]