from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from music.models import Song, Album, Artist
from myAdmin.forms import *
from utils.views import *
import eyed3
# Create your views here.

User = get_user_model()
class HomeView(LoginRequiredMixin, View):
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
            songObj.artist = self.request.user
            songObj.save()
            return redirect('myAdmin:SongMeta')

        else:
            return render(request, self.template_name, {'form': form, 'msg_error': "There Seems to be Some Problem. Please See Below !"})

class SongView(ArtistsMixin, ListView):
    template_name =  'music/song_list.html'
    pagninated = 40

    def get_queryset(self):
        qs = Song.objects.all()
        print(qs)
        return qs

class SongCreate(ArtistsMixin, CreateView):
    model = Song
    fields = ['artist', 'album', 'audio']
    success_url = reverse_lazy('myAdmin:SongMeta')

class SongDelete(ArtistsMixin, DeleteView):
    model = Song
    success_url = reverse_lazy('myAdmin:SongList')

class SongUpdate(UpdateView):
    model = Song
    fields = '__all__'
    success_url = reverse_lazy('myAdmin:SongList')

def songmeta(self):
    model = Album
    for song in Song.objects.all():
        temp=eyed3.load(song.audio.url)
        song.playback_time=temp.info.time_secs
        song.title=temp.tag.title
        song.genre=str(temp.tag.genre)
        song.save()

    return redirect('myAdmin:SongList')
