from django.conf.urls import url, include
from myAdmin import views
from django.conf import settings
app_name='myAdmin'

if settings.DEBUG:
    urlpatterns = [
        url(r'^$', views.HomeView.as_view(), name='myadmin'),

        url(r'^album/$', views.AlbumView.as_view(), name='AlbumList'),
        url(r'^song/$', views.SongView.as_view(), name='SongList'),
        url(r'^artist/$', views.ArtistView.as_view(), name='ArtistList'),
        url(r'^temp/$', views.songmeta, name='SongMeta'),
        url(r'album/add/$', views.AlbumAddView.as_view(), name='album_add'),
        url(r'song/add/$', views.SongCreate.as_view(), name='song_add'),
        url(r'artist/add/$', views.ArtistCreate.as_view(), name='artist_add'),

        url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),
        url(r'song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song_update'),
        url(r'artist/(?P<pk>[0-9]+)/$', views.ArtistUpdate.as_view(), name='artist_update'),

        url(r'album/delete/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album_delete'),
        url(r'song/delete/(?P<pk>[0-9]+)/$', views.SongDelete.as_view(), name='song_delete'),
        url(r'artist/delete/(?P<pk>[0-9]+)/$', views.SongDelete.as_view(), name='artist_delete'),
    ]
