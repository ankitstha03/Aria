from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from music.models import Song, Album
from authentication.models import UserProfiles
# Create your views here.

class Profile(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = UserProfiles


def home(request):
    return HttpResponseRedirect(reverse('profile_display:profile', args=[request.user.id]))

