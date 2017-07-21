from django.conf.urls import url, include
from django.contrib.auth.views import LoginView
from. import views
app_name = 'authen'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
]
