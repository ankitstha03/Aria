from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
# This line allows you to import the necessary functions of the authentication module.
def page(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'en/public/connection.html')
                else:
                    return render(request, 'en/public/LOGIN.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'en/public/LOGIN.html', {'error_message': 'Invalid login'})
    return render(request, 'en/public/LOGIN.html')
