from django.conf.urls import url, include
from myAdmin import views
from django.conf import settings

if settings.DEBUG:
    urlpatterns = [
        url(r'^$',views.home, name='myadmin'),
        url(r'^album/$', views.AlbumView.as_view(), name='AlbumList'),
        url(r'^song/$', views.SongView.as_view(), name='SongList'),
        url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),
        url(r'song/add/$', views.SongCreate.as_view(), name='song_add'),
        url(r'album/(?P<factory_id>[0-9a-f-]+)/$', views.AlbumUpdate.as_view(), name='album_update'),
        url(r'song/(?P<factory_id>[0-9a-f-]+)/$', views.SongUpdate.as_view(), name='song_update'),
        url(r'album/delete/(?P<factory_id>[0-9a-f-]+)/$', views.AlbumDelete.as_view(), name='album_delete'),
        url(r'song/delete/(?P<factory_id>[0-9a-f-]+)/$', views.SongDelete.as_view(), name='song_delete'),
    ]
