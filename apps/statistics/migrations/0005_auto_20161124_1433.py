# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0004_auto_20161123_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='server_id',
            field=models.IntegerField(db_index=True),
        ),
    ]