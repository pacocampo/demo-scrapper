# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_web_checker_runtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='webToScrap',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='data.WebToScrap'),
            preserve_default=False,
        ),
    ]
