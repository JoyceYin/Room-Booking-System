# Generated by Django 2.2.12 on 2020-05-27 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0008_auto_20200527_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='RID_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.room_info'),
        ),
    ]
