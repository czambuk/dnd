# Generated by Django 3.0.3 on 2020-05-17 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('char_app', '0006_auto_20200517_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='basic_class',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basic_class', to='char_app.Classes'),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='char_app.Races'),
        ),
    ]