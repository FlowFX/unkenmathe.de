# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_auto_20170829_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
