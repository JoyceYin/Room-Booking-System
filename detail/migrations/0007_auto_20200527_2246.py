# Generated by Django 2.2.12 on 2020-05-27 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0006_auto_20200527_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='RID',
            field=models.IntegerField(),
        ),
    ]
