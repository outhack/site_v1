# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_datapoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='options',
            field=models.CharField(default='', max_length=1028),
        ),
    ]