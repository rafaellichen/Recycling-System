# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainRecycleApp', '0010_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='idc',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='description',
            name='pickup_info',
            field=models.TextField(blank=True),
        ),
    ]
