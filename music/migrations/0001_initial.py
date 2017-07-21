# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0004_auto_20170720_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('tag', models.CharField(max_length=50, verbose_name='Tag')),
                ('Location', models.CharField(max_length=100, verbose_name='Location')),
                ('familiarity', models.CharField(max_length=10, verbose_name='Familiarity')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('name', models.CharField(max_length=50, verbose_name='Playlist Name')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('playback_time', models.CharField(max_length=5, verbose_name='PlayBackTime')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='song_id',
            field=models.ManyToManyField(to='music.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.UserProfiles'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist'),
        ),
    ]
