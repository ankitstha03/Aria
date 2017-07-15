from django.conf.urls import url, include
from myAdmin import views


urlpatterns = [
    url(r'^$',views.home, name='myadmin'),
    url(r'^album/$', views.AlbumView.as_view(), name='AlbumList'),
    url(r'^song/$', views.SongView.as_view(), name='SongList'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),
    url(r'song/add/$', views.SongCreate.as_view(), name='song_add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),
    url(r'song/(?P<pk>[0-9]+)/$', views.SongUpdate.as_view(), name='song_update'),
    url(r'album/delete/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album_delete'),
    url(r'song/delete/(?P<pk>[0-9]+)/$', views.SongDelete.as_view(), name='song_delete'),
]

