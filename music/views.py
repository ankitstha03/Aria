from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from .models import Album, Song, Playlist
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from .forms import *
from authentication.forms import *
from myAdmin.forms import *
from utils.views import *
# Create your views here
#class PlaylistView(UsersMixin,ListView):
#    model = Playlist
#
#class SongList(View):
#    def get(self, request, *args, **kwargs):
#        song = Song()
#        songall = Song.objects.all()
#        return  render(request, 'music/song_list.html', {'song':song})
#
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'sitearia/base1.html')

class AlbumView(ListView):
    template_name =  'music/album_list2.html'
    model = Album


class AlbumDetails(DetailView):
    model = Album

class ArtistView(ListView):
    template_name =  'music/artist_list2.html'
    model = Artist



class SongView(ListView):
    template_name =  'music/song_list2.html'
    pagninated = 40

def ArtistAlbum(request):
    if not request.user.is_authenticated():
        return redirect('authen:register')
    else:
        albums = Album.objects.filter(artist=request.user)
        addAlbumForm = AlbumForm()
        form = AlbumForm(request.POST)
        if form.is_valid():
            albumObj = form.save(commit=False)
            albumObj.artist = request.user
            albumObj.cover = request.FILES['cover']
            albumObj.save()
            return render(request, 'music/album_list3.html', {'albums': albums, 'form':addAlbumForm})
        return render(request, 'music/album_list3.html', {'albums': albums, 'form':addAlbumForm})


def album_detail(request, album_id):
    if not request.user.is_authenticated():
        return redirect('authen:register')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'music/album_detail.html', {'album': album, 'user': user})

class PlaylistAddView(UsersMixin, View):
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
    template_name =  'music/playlist_list2.html'
    model = Playlist


class PlaylistCreate(CreateView):
    model = Playlist
    fields = '__all__'

    success_url = reverse_lazy('music:Playlist')

class PlaylistDelete(DeleteView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('music:Playlist')

class PlaylistUpdate(UpdateView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('music:Playlist')

def PlaylistPlay(request,playlist_id):
    playlist = get_object_or_404(Playlist,pk=playlist_id)
    return render_to_response('music/playlist_play.html',{
    "playlist" : playlist
    })
