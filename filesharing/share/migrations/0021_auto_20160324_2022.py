# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 20:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0020_file_expires_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='date_uploaded',
        ),
        migrations.RemoveField(
            model_name='file',
            name='time_uploaded',
        ),
        migrations.AlterField(
            model_name='file',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 24, 20, 27, 40, 893985, tzinfo=utc)),
        ),
    ]