"""Implementation of models from ERD"""

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.models import CreationModificationDateMixin
from django.contrib import admin
from authentication.models import UserProfiles
class Artist(CreationModificationDateMixin):
    """
    A table to store the artist information
    """
    name = models.CharField(_("Name"), max_length=50)
    tag = models.CharField(_("Tag"), max_length=50)
    Location = models.CharField(_("Location"), max_length=100)
    familiarity = models.CharField(_("Familiarity"), max_length=10)
    artist_id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.name

class Album(CreationModificationDateMixin):
    """
    A table storing the album related information like name, year, genre, and artist_id
    """
    name = models.CharField(_("Name"), max_length=50)
    genre = models.CharField(_("Genre"), max_length=50)
    year = models.IntegerField(_("Year"))
    artist_id = models.ForeignKey(Artist)
    album_id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.name


class Song(CreationModificationDateMixin):
    """
    A song table storing title, genre, playback time, album id
    """
    title = models.CharField(_("Title"), max_length=200)
    genre = models.CharField(_("Genre"), max_length=50)
    playback_time = models.CharField(_("PlayBackTime"), max_length=5)
    artist_id = models.ForeignKey(Artist)
    album_id = models.ForeignKey(Album)
    song_id = models.PositiveIntegerField(primary_key=True, default=1)
    def __str__(self):
        return self.title

class playlist(CreationModificationDateMixin):
    """
    This contains the playlist name, the songs included in the playlist, and the user_id
    for the given Playlist
    """
    name = models.CharField(_("Playlist Name"), max_length=50)
    song_id = models.ManyToManyField(Song)
    user_id = models.ForeignKey(UserProfiles)
    playlist_id = models.PositiveIntegerField(primary_key=True, default=1)

    def __str__(self):
        return self.name
from django.contrib import admin


class SoftDeleteAdmin(admin.ModelAdmin):
    list_display = ('album_id', 'deleted_at',)
    list_filter = ('deleted_at',)

    def queryset(self, request):
        qs = Album.all_objects.all()
        if request.user.is_superuser:
            return qs


