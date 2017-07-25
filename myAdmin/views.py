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
from django.contrib.auth import get_user_model
from music.models import Song, Album, Artist
from myAdmin.forms import AlbumForm
from music.views import *
# Create your views here.
User = get_user_model()
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'layouts/admin/base.html')

class AlbumView(ListView):
    model = Album
    paginated = 25

class AlbumDetails(DetailView):
    model = Album
class AlbumAddView(ArtistsMixin, View):
   template_name = 'music/album_form.html'

   def get(self, request, *args, **kwargs):
       addAlbumForm = AlbumForm()
       return render(request, self.template_name, {'form': addAlbumForm})

   def post(self, request, *args, **kwargs):
       form = AlbumForm(request.POST)
       if form.is_valid():
           albumObj = form.save(commit=False)
           albumObj.artist = self.request.user
           albumObj.save()
           return HttpResponseRedirect('/')

       else:
           return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})

class AlbumCreate(CreateView):
    model = Album
    fields = ['name', 'genre', 'year']
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
