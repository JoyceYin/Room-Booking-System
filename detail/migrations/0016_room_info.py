# Generated by Django 2.2.12 on 2020-05-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0015_delete_room_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='room_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RID', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=25)),
                ('accommodates', models.IntegerField()),
                ('stars', models.DecimalField(decimal_places=1, max_digits=3)),
                ('bathrooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('amenities', models.TextField()),
                ('price', models.IntegerField()),
                ('image_url', models.URLField(blank=True, default=' ')),
            ],
        ),
    ]
