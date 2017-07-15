from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
# This line allows you to import the necessary functions of the authentication module.
def page(request):
    if request.POST:
        form = Form_connection(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
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

class Form_connection(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(Form_connection, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong login or passwsord")
        return self.cleaned_data
