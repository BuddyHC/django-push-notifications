# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 08:50
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='registration_id',
            field=models.CharField(max_length=200, unique=True, verbose_name='Registration ID'),
        ),
    ]
