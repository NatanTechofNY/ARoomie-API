# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-26 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroomieapp', '0021_auto_20170103_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='device_token',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
