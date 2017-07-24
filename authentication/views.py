from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView
from authentication.models import UserProfiles
from authentication.forms import Form_connection, Form_inscription
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
    if request.POST:
        form = Form_connection(request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            # This line verifies that the username exists and the password is correct.
            if user:
                login(request, user)
	# In this line, the login() function allows the user to connect.
                if request.GET.get('next') is not None:
                    return redirect(request.GET['next'])
        else:
            return render(request, 'en/public/connection.html', {'form' : form})
    else:
        form = Form_connection()
    return render(request, 'en/public/connection.html', {'form' : form})

def signup_page(request):
    if request.POST:
        form = Form_inscription(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User.objects.create_user(username=login, email=email, password=password)
            new_user.is_active = True
            new_user.last_name = name
            new_user.save()
            user = UserProfiles(user=new_user)
            user.save()
            return HttpResponse("User Created")
        else:
            return render(request, 'en/public/create_user.html', {'form' : form})
    else:
        form = Form_inscription()
    form = Form_inscription()
    return render(request, 'en/public/create_user.html', {'form' : form})

def page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index1'))

