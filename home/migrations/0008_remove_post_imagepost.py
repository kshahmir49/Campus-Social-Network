# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 09:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180328_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagepost',
        ),
    ]