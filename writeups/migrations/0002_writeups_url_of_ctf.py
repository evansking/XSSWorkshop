# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 04:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('writeups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writeups',
            name='url_of_CTF',
            field=models.URLField(default=datetime.datetime(2016, 7, 12, 4, 23, 47, 368150, tzinfo=utc)),
            preserve_default=False,
        ),
    ]