# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecyclingCenters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.TextField()),
                ('website', models.TextField()),
                ('timetable', models.TextField()),
            ],
        ),
    ]