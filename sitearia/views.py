from django.shortcuts import render
from music.models import *
from django.db.models import Q
# Create your views here.

def index1(request):
    query = request.GET.get("q")
    albums = Album.objects.all()
    song_results = Song.objects.all()
    artists=Artist.objects.all()
    playlists=Playlist.objects.all()

    if query:
        albums = albums.filter(
            Q(name__icontains=query)
        ).distinct()
        song_results = song_results.filter(
            Q(title__icontains=query)
        ).distinct()
        artists = artists.filter(
            Q(name__icontains=query)
        ).distinct()
        playlists = playlists.filter(
            Q(name__icontains=query)
        ).distinct()
        return render(request, 'music/search.html', {
            'albums': albums,
            'songs': song_results,
            'artists':artists,
            'playlists':playlists,
        })
    else:
        return render(request, 'sitearia/HOME.html')
