# Generated by Django 2.2.12 on 2020-05-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20200527_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(default='Nothing', max_length=1000),
        ),
    ]
