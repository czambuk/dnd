# Generated by Django 3.0.3 on 2020-05-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char_app', '0010_auto_20200522_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='hero_classes',
            field=models.ManyToManyField(null=True, to='char_app.Classes'),
        ),
    ]