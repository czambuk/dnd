# Generated by Django 3.0.3 on 2020-04-13 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns_diary', '0004_auto_20200413_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='players',
        ),
    ]
