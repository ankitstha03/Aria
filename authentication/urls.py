from django.conf.urls import url, include
from authentication.views import *
from django.contrib.auth.views import LoginView

app_name='authen'

urlpatterns = [
    url(r'^login/$', login_page, name='login'),
    url(r'^$', signup_page, name="register"),
    url(r'^profile$', ProfileView.as_view(), name='index'),
    url(r'^home$', HomeView.as_view(), name='home'),
    url(r'(?P<pk>\d+)/$',ProfileView.as_view(), name='profile'),


]
