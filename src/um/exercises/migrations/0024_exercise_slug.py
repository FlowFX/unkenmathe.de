# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0023_auto_20171004_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='slug',
            field=models.SlugField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
