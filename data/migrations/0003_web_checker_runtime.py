# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
        ('data', '0002_webtoscrap'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='checker_runtime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_scraper.SchedulerRuntime'),
        ),
    ]
