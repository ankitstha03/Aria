from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from music.models import Song, Album
from authentication.models import UserProfiles
# Create your views here.

class Profile(DetailView):
    model = UserProfiles

