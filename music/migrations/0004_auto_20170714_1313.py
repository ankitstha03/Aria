# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20170708_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deteled date'),
        ),
        migrations.AddField(
            model_name='artist',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deteled date'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deteled date'),
        ),
        migrations.AddField(
            model_name='song',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='deteled date'),
        ),
    ]