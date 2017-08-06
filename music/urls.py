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
    url(r'^album/(?P<album_id>[0-9]+)/as/(?P<song_id>[0-9]+)/$', views.albumer, name='albumer'),
    url(r'^song/(?P<song_id>[0-9]+)/$', views.songer, name='songer'),
    url(r'^playlist/(?P<playlist_id>[0-9]+)/$', views.playlist_detail2, name='playlist_detail2'),
    url(r'^playlist/(?P<playlist_id>[0-9]+)/as/(?P<song_id>[0-9]+)/$', views.playlister, name='playlister'),
    url(r'^userplaylist/(?P<playlist_id>[0-9]+)/$', views.playlist_detail, name='playlist_detail'),
    url(r'^userplaylist/(?P<playlist_id>[0-9]+)/add/(?P<song_id>[0-9]+)/$', views.add_playlist, name='add_playlist'),
    url(r'^userplaylist/(?P<playlist_id>[0-9]+)/remo/(?P<song_id>[0-9]+)/$', views.remove_playlist, name='remove_playlist'),
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.artist_detail, name='artist_detail'),
    url(r'^artist/(?P<artist_id>[0-9]+)/as/(?P<song_id>[0-9]+)/$', views.artister, name='artister'),
    url(r'userplaylist/$', views.UserPlayList, name='UserPlayList'),
    url(r'playlist/(?P<pk>[0-9]+)/$', views.PlaylistUpdate.as_view(), name='playlist_update'),
    url(r'userplaylist/delete/(?P<playlist_id>[0-9]+)/$', views.delete_playlist, name='delete_playlist'),
    url(r'playlist/(?P<playlist_id>[0-9]+)/play/$', views.PlaylistPlay, name='playlist_play'),
    url(r'^artistsection/(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^artistsection/(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    #url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
    #url(r'^songs/$', views.SongList.as_view(), name='song_list'),
]
