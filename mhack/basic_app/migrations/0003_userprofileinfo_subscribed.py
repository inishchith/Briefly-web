# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-03 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_userprofileinfo_idno'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='subscribed',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]
