from django import forms
from .models import *
from django.contrib.auth import get_user_model
from music.models import Song, Album, Artist
from music.views import *

User = get_user_model()

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['artist']

   # Adding Classes to each for CSS styling
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['album', 'audio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class PlaylistForm(forms.ModelForm):
   class Meta:
       model = Playlist
       exclude = ['user']

   # Adding Classes to each for CSS styling
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in iter(self.fields):
           self.fields[field].widget.attrs.update({
               'class': 'form-control'
           })
