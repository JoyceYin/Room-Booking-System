# Generated by Django 2.2.12 on 2020-05-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0009_remove_book_outdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='RID',
            field=models.IntegerField(),
        ),
    ]
