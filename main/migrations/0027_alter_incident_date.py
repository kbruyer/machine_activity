# Generated by Django 4.0.6 on 2022-08-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_incident_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]