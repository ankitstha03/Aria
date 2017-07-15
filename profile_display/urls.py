from django.conf.urls import url
from . import views
app_name = 'profile_display'

urlpatterns = [
	url(r'^$', views.Profile.as_view(), name='index'),
        url(r'^home$', views.home, name='home'),
	url(r'(?P<pk>\d+)/$', views.Profile.as_view(), name='profile'),

]
