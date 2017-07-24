from django.conf.urls import url, include
from authentication.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    url('^$',LoginView.as_view(template_name='en/public/connection.html'), name="login"),
    url(r'^signup$', signup_page, name="create_user"),
    url(r'^profile$', ProfileView.as_view(), name='index'),
    url(r'^home$', HomeView.as_view(), name='home'),
    url(r'(?P<pk>\d+)/$',ProfileView.as_view(), name='profile'),


]
