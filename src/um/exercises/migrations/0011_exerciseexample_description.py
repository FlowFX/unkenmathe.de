# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_exerciseexample'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseexample',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
    ]
