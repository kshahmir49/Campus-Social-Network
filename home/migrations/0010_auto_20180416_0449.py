# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_post_imagepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagepost',
            field=models.FileField(default='null', upload_to='static/media'),
        ),
    ]
