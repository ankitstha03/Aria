# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified_at', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('year', models.IntegerField(verbose_name='Year')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified_at', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('tag', models.CharField(max_length=50, verbose_name='Tag')),
                ('Location', models.CharField(max_length=100, verbose_name='Location')),
                ('familiarity', models.CharField(max_length=10, verbose_name='Familiarity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified_at', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('name', models.CharField(max_length=50, verbose_name='Playlist Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified_at', models.DateTimeField(editable=False, null=True, verbose_name='modification date and time')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deteled date')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('genre', models.CharField(max_length=50, verbose_name='Genre')),
                ('playback_time', models.CharField(max_length=5, verbose_name='PlayBackTime')),
                ('audio', models.FileField(default='songs/test.mp3', upload_to='songs')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='music.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.UserProfiles'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist'),
        ),
    ]
