# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 04:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0009_auto_20170625_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='ProId',
        ),
    ]