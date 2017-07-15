from django.contrib import admin
from .models import Album
from .models import Song
from .models import Artist
from .models import playlist
from .models import SoftDeleteAdmin

#admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(playlist)
admin.site.register(Album, SoftDeleteAdmin)
