# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-19 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0011_auto_20171019_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]