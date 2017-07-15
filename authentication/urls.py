from django.conf.urls import url, include
from authentication.views import connection,create_user,logout


urlpatterns = [
    url(r'^$', connection.page , name="public_connection"),
    url(r'^new_user$', create_user.page, name="create_user"),
    url(r'^logout$', logout.page, name="logout"),
]
