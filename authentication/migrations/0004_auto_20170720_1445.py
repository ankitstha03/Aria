# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20170714_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofiles',
            old_name='new_userid',
            new_name='id',
        ),
    ]
