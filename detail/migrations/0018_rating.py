# Generated by Django 2.2.12 on 2020-05-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0017_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RID', models.IntegerField()),
                ('UID', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
