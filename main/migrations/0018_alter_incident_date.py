# Generated by Django 4.0.6 on 2022-08-05 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_incident_category_alter_incident_gamename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]