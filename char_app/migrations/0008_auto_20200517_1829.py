# Generated by Django 3.0.3 on 2020-05-17 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('char_app', '0007_auto_20200517_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='alignment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='char_app.Alignments'),
        ),
    ]
