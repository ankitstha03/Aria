from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from music.models import Song, Album
# Create your views here.
class AlbumView(ListView):
    model = Album
    paginated = 25

class SongView(DetailView):
    model = Song

class AlbumCreate(CreateView):
    model = Song
    fields = '__all__'
class AlbumUpdate(UpdateView):
    model = Song
    fields = '__all__'

class AlbumDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('Music')
