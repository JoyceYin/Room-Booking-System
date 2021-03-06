# Generated by Django 2.2.12 on 2020-05-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200526_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='host_info',
            name='image_url',
            field=models.URLField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='host_info',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
