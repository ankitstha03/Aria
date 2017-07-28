from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
app_name='music'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='music'),
    url(r'^album/$', views.AlbumView.as_view(), name='AlbumList'),
    url(r'^song/$', views.SongView.as_view(), name='SongList'),
    url(r'^artist/$', views.ArtistView.as_view(), name='ArtistList'),
    url(r'^playlist/$', views.PlaylistView.as_view(), name='PlayList'),
    url(r'^artistsection/$', views.ArtistAlbum, name='ArtistAlbum'),
    url(r'^artistsection/(?P<album_id>[0-9]+)/$', views.album_detail, name='album_detail'),
    url(r'^album/(?P<album_id>[0-9]+)/$', views.album_detail2, name='album_detail2'),
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.artist_detail, name='artist_detail'),
    url(r'playlist/add/$', views.PlaylistCreate.as_view(), name='playlist_add'),
    url(r'playlist/(?P<pk>[0-9]+)/$', views.PlaylistUpdate.as_view(), name='playlist_update'),
    url(r'playlist/delete/(?P<pk>[0-9]+)/$', views.PlaylistDelete.as_view(), name='playlist_delete'),
    url(r'playlist/(?P<playlist_id>[0-9]+)/play/$', views.PlaylistPlay, name='playlist_play'),
    #url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
    #url(r'^songs/$', views.SongList.as_view(), name='song_list'),
]
