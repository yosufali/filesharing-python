# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0017_file_urlname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='urlname',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
