# Generated by Django 4.0.6 on 2022-08-15 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_incident_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='gameName',
            new_name='game_Name',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='serialNumber',
            new_name='serial_Number',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='techName',
            new_name='tech_Name',
        ),
    ]