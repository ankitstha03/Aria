from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from .models import Album, Song, Playlist
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from .forms import *
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

def PlaylistPlay(request,playlist_id):
    playlist = get_object_or_404(Playlist,pk=playlist_id)
    return render_to_response('music/playlist_play.html',{
    "playlist" : playlist
    })
