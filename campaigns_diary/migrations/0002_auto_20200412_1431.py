# Generated by Django 3.0.3 on 2020-04-12 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns_diary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaignentry',
            old_name='campaign',
            new_name='chosen_campaign',
        ),
    ]