from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from music.models import *
from myAdmin.forms import *
from utils.views import *
import eyed3
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



User = get_user_model()
class HomeView(ArtistsMixin, View):
    def get(self, request):
        return render(request, 'layouts/admin/base.html')

class AlbumView(ArtistsMixin, ListView):
    template_name =  'music/album_list.html'
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
            albumObj.cover = request.FILES['cover']
            albumObj.save()
            return redirect('myAdmin:AlbumList')

        else:
            return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})

class AlbumUpdate(ArtistsMixin, UpdateView):
    model = Album
    fields = '__all__'

class AlbumDelete(ArtistsMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('myAdmin:AlbumList')

class PlaylistView(ArtistsMixin, ListView):
    template_name =  'music/play_list2.html'
    model = Playlist
    context_object_name = "playlist_list"
    paginated = 25

class PlaylistDetails(DetailView):
    model = Playlist

class PlaylistAddView(ArtistsMixin, View):
    template_name = 'music/play_form.html'
    def get(self, request, *args, **kwargs):
        addAlbumForm = PlaylistForm()
        return render(request, self.template_name, {'form': addAlbumForm})

    def post(self, request, *args, **kwargs):
        form = PlaylistForm(request.POST)
        if form.is_valid():
            albumObj = form.save(commit=False)
            albumObj.user = self.request.user
            albumObj.pcover = request.FILES['pcover']
            albumObj.save()
            return redirect('myAdmin:PlayList')

        else:
            return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})

class PlaylistUpdate(ArtistsMixin, UpdateView):
    model = Playlist
    fields = '__all__'
    success_url = reverse_lazy('myAdmin:PlayList')

class PlaylistDelete(ArtistsMixin, DeleteView):
    model = Playlist
    success_url = reverse_lazy('myAdmin:PlayList')

class ArtistView(AdministratorOnlyMixin, ListView):
    template_name =  'music/artist_list.html'
    model = Artist

class ArtistDetails(AdministratorOnlyMixin, DetailView):
    model = Artist

class ArtistCreate(AdministratorOnlyMixin, CreateView):
    model = Artist
    fields = '__all__'
    success_url = reverse_lazy('myAdmin:ArtistList')

class ArtistUpdate(AdministratorOnlyMixin, UpdateView):
    model = Artist
    fields = '__all__'
    success_url = reverse_lazy('myAdmin:ArtistList')

class ArtistDelete(AdministratorOnlyMixin, DeleteView):
    model = Artist
    success_url = reverse_lazy('myAdmin:ArtistList')

class SongAddView(ArtistsMixin, View):
    template_name = 'music/song_form.html'
    def get(self, request, *args, **kwargs):
        addSongForm = SongForm()
        return render(request, self.template_name, {'form': addSongForm})

    def post(self, request, *args, **kwargs):
        form = SongForm(request.POST)
        if form.is_valid():
            songObj =form.save(commit=False)
            songObj.audio = request.FILES['audio']
            songObj.save()
            temp=eyed3.load(songObj.audio.url)
            songObj.playback_time=temp.info.time_secs
            songObj.title=temp.tag.title
            songObj.genre=str(temp.tag.genre)
            songObj.save()
            return redirect('myAdmin:SongList')

        else:
            return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})

class SongView(ArtistsMixin, ListView):
    template_name =  'music/song_list.html'
    pagninated = 40

    def get_queryset(self):
        qs = Song.objects.all()
        print(qs)
        return qs



class SongDelete(ArtistsMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('myAdmin:SongList')

class SongUpdate(UpdateView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('myAdmin:SongList')
