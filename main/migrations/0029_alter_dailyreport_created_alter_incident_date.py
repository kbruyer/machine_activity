# Generated by Django 4.0.6 on 2022-08-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_dailyreport_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyreport',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
