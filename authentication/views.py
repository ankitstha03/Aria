from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView
from authentication.models import UserProfiles
from .forms import *
from music.models import *

#from music.models import Song, Album, playlist
# This line imports the Django forms package
# This line allows you to import the necessary functions of the authentication module.
class ProfileView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = UserProfiles
#class PlaylistCreation(View):
#    def get(self,request)

class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args):
        return HttpResponseRedirect(reverse('profile', args=[request.user.id]))

def login_page(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        'error_message': 'Invalid Login',
    }
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index1')
            else:
                return render(request, 'en/public/LOGIN.html', context)
        else:
            return render(request, 'en/public/LOGIN.html',context)
    return render(request, 'en/public/LOGIN.html',context)

def signup_page(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        confirm_password=form.cleaned_data['confirm_password']
        password = form.cleaned_data['password']
        user.set_password(password)
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords are not identical.")
            return render(request, 'en/public/LOGIN.html', context)
        user.save()
        user2 = UserProfiles(user=user, bio="ankit is", location="nepal")
        user2.save()
        arti=Artist(name=user.first_name, Location="nepal")
        arti.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index1')
    context = {
        "form": form,
    }
    return render(request, 'en/public/LOGIN.html', context)

def logout_page(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('index1')
