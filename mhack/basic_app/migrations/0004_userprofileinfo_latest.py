# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-03 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_userprofileinfo_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='latest',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]