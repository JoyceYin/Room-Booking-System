# Generated by Django 2.2.12 on 2020-05-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0007_auto_20200527_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='UID',
            field=models.IntegerField(),
        ),
    ]
