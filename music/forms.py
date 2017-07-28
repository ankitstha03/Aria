from django import forms
from .models import *
from django.contrib.auth import get_user_model
from music.views import *

User = get_user_model()

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

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['name', 'genre', 'year', 'cover']
