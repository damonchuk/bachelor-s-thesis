# Generated by Django 4.2 on 2023-04-22 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cars_photo_alter_cars_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
    ]
