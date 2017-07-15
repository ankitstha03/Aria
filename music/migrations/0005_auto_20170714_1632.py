# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170714_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='song',
            name='deleted',
        ),
        migrations.AddField(
            model_name='album',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date'),
        ),
        migrations.AddField(
            model_name='artist',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date'),
        ),
        migrations.AddField(
            model_name='song',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date'),
        ),
    ]
