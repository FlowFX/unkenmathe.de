# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0021_auto_20171004_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
