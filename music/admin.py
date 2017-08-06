from django.contrib import admin
from .models import Album
from .models import Song
from .models import Artist
from .models import Playlist
from .models import PlayCount

#admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Playlist)
admin.site.register(Album)
admin.site.register(PlayCount)
