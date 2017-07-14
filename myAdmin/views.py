"""
File: views.py
Author: Shailesh Mishra
Github: https://github.com/rezera
Description: A views for implementation of CRUD.
"""

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from music.models import Song, Album
# Create your views here.
class AlbumView(ListView):
    model = Album
    paginated = 25

class AlbumDetails(DetailView):
    model = Album

class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'

class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__'

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('AlbumList')

class SongView(ListView):
    model = Song
    pagninated = 40

class SongCreate(CreateView):
    model = Song
    fields = '__all__'
