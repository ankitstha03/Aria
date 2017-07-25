from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
app_name='music'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='music/index.html'), name='index'),

    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    #url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
]
