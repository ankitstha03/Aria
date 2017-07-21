from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django import forms
from django.core.urlresolvers import reverse
from authentication.models import UserProfiles


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'en/public/LOGIN.html', context)

def login_user(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        'error_message': 'Your account has been disabled',
    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'sitearia/HOME.html')
            else:
                return render(request, 'en/public/LOGIN.html', context)
        else:
            return render(request, 'en/public/LOGIN.html',context)
    return render(request, 'en/public/LOGIN.html',context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        confirm_password=form.cleaned_data['confirm_password']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords are not identical.")
            return render(request, 'en/public/LOGIN.html', context)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'sitearia/HOME.html')
    context = {
        "form": form,
    }
    return render(request, 'en/public/LOGIN.html', context)
