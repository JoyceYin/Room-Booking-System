# Generated by Django 2.2.12 on 2020-05-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_auto_20200526_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_id',
            name='UID',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
