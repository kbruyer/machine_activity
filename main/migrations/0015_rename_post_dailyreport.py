# Generated by Django 4.0.6 on 2022-08-02 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_post_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='DailyReport',
        ),
    ]
