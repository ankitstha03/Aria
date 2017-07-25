
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, CreateView
from .models import Album, Song, Playlist
from django.core.urlresolvers import reverse_lazy
from utils.views import *
# Create your views here
class PlaylistView(UsersMixin,ListView):
    model = Playlist

class PlaylistCreate(UsersMixin,CreateView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('music:playlist')
