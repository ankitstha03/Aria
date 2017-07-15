from django.conf.urls import url, include
from authentication.views import connection,create_user,logout
from django.contrib.auth.views import LoginView

urlpatterns = [
    url('^$',LoginView.as_view(template_name='en/public/connection.html'), name="login"),
    url(r'^signup$', create_user.page, name="create_user"),
]
