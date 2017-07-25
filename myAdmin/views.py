"""
File: views.py
Author: Shailesh Mishra
Github: https://github.com/rezera
Description: A views for implementation of CRUD.
"""

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from music.models import Song, Album, Artist
# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'layouts/admin/base.html')

class AlbumView(ListView):
    model = Album
    paginated = 25

class AlbumDetails(DetailView):
    model = Album

class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'
    success_url = reverse_lazy('song_add')

class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__'

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('AlbumList')

class ArtistView(ListView):
    model = Artist

class ArtistDetails(DetailView):
    model = Artist

class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'
    success_url = reverse_lazy('ArtistList')

class ArtistUpdate(UpdateView):
    model = Artist
    fields = '__all__'
    success_url = reverse_lazy('ArtistList')

class ArtistDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy('ArtistList')


class SongView(ListView):
    template_name =  'music/song_list.html'
    pagninated = 40

    def get_queryset(self):
        qs = Song.objects.all()
        print(qs)
        return qs

class SongCreate(CreateView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('SongList')

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('SongList')

class SongUpdate(UpdateView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('SongList')
