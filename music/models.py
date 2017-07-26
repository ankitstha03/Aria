"""Implementation of models from ERD"""



from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.models import CreationModificationDateMixin
from django.contrib import admin
import uuid
from authentication.models import UserProfiles
from django.contrib.auth import get_user_model

User = get_user_model()
class Artist(CreationModificationDateMixin):
    """
    A table to store the artist information
    """
    name = models.CharField(_("Name"), max_length=50)
    tag = models.CharField(_("Tag"), max_length=50)
    Location = models.CharField(_("Location"), max_length=100)
    familiarity = models.CharField(_("Familiarity"), max_length=10)

    def __str__(self):
        return self.name

class Album(CreationModificationDateMixin):
    """
    A table storing the album related information like name, year, genre, and artist_id
    """
    name = models.CharField(_("Name"), max_length=50)
    genre = models.CharField(_("Genre"), max_length=50)
    year = models.IntegerField(_("Year"))
    artist = models.ForeignKey(User)

    def __str__(self):
        return self.name
class Song(CreationModificationDateMixin):
    """
    A song table storing title, genre, playback time, album id
    """
    title = models.CharField(_("Title"), max_length=200)
    genre = models.CharField(_("Genre"), max_length=50)
    playback_time = models.CharField(_("PlayBackTime"), max_length=5)
    artist = models.ForeignKey(User)
    album = models.ForeignKey(Album)
    audio = models.FileField(upload_to="songs",default = "songs/test.mp3")
    def __str__(self):
        return self.title

class Playlist(CreationModificationDateMixin):
    """
    This contains the playlist name, the songs included in the playlist, and the user_id
    for the given Playlist
    """
    name = models.CharField(_("Playlist Name"), max_length=50)
    songs = models.ManyToManyField(Song, blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name
