# Generated by Django 2.2.12 on 2020-05-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20200527_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='street',
            field=models.CharField(max_length=500),
        ),
    ]
