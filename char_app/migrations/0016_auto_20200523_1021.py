# Generated by Django 3.0.3 on 2020-05-23 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('char_app', '0015_auto_20200523_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='passive_perception_prof',
            new_name='passive_perception',
        ),
    ]
