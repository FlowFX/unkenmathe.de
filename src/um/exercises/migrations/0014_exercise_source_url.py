# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0013_exercise_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='source_url',
            field=models.URLField(blank=True),
        ),
    ]