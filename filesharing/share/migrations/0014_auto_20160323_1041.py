# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0013_auto_20160323_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='time_uploaded',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
