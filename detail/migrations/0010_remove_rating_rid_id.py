# Generated by Django 2.2.12 on 2020-05-27 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0009_auto_20200527_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='RID_id',
        ),
    ]
