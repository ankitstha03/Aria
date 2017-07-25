from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
app_name='music'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='music/index.html'), name='index'),

    url(r'^playlist/$', views.PlaylistView.as_view(), name='playlist'),
    url(r'playlist/add/$', views.PlaylistAddView.as_view(), name='playlist_add'),
    #url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
    #url(r'^songs/$', views.SongList.as_view(), name='song_list'),
]
