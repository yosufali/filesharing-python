# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0018_auto_20160324_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
