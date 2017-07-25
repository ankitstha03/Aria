
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, CreateView
from .models import Album, Song, Playlist
from django.core.urlresolvers import reverse_lazy
from braces.views import GroupRequiredMixin, AnonymousRequiredMixin

class AdministratorOnlyMixin(GroupRequiredMixin):
    group_required = ["Administrator"]
    login_url = '/myadmin/login/'

class ArtistsMixin(GroupRequiredMixin):
    group_required = ["Administrator","Artists"]
    login_url = '/myadmin/login/'

class UsersMixin(GroupRequiredMixin):
    group_required = ["Users", "Administrator", "Artists"]
    login_url = '/myadmin/login/'

# Create your views here
class PlaylistView(AdministratorOnlyMixin,ListView):
    model = Playlist

class PlaylistCreate(AdministratorOnlyMixin,CreateView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('music:playlist')
