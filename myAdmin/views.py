from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from music.models import Song, Album, Artist
from myAdmin.forms import *
from utils.views import *
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
            return HttpResponseRedirect(reverse('AlbumList'))

        else:
            return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})

class SongAddView(ArtistsMixin, View):
    template_name = 'music/song_form.html'
    def get(self, request, *args, **kwargs):
        addSongForm = SongForm()
        return render(request, self.template_name, {'form': addSongForm})

    def post(self, request, *args, **kwargs):
        form = SongForm(request.POST)
        if form.is_valid():
            songObj = form.save(commit=False)
            songObj.artist = self.request.user
            songObj.save()
            return HttpResponseRedirect(reverse('song_add'))

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

class PlaylistAddView(ArtistsMixin, View):
   template_name = 'music/playlist_form.html'

   def get(self, request, *args, **kwargs):
       addPlaylistForm = PlaylistForm()
       return render(request, self.template_name, {'form': addPlaylistForm})

   def post(self, request, *args, **kwargs):
       form = PlaylistForm(request.POST)
       if form.is_valid():
           playlistObj = form.save(commit=False)
           playlistObj.user = self.request.user
           playlistObj.save()
           return HttpResponseRedirect(reverse_lazy('PlaylistList'))

       else:
           return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})


class PlaylistView(ListView):
    model = Playlist
    fields = '__all__'

class PlaylistCreate(CreateView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('PlaylistList')

class PlaylistDelete(DeleteView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('PlaylistList')

class PlaylistUpdate(UpdateView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('PlaylistList')
