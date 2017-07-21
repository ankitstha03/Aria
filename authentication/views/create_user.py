from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from authentication.models import UserProfiles
from django.contrib.auth.models import User
# This line imports the Django forms package
class Form_inscription(forms.Form):
	# name     = forms.CharField(label="Name", max_length=30, error_messages=error_name)
    name = forms.CharField(label="Name", max_length=30)
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
    # We add another field for the password. This field will be used to avoid typos from the user. If both passwords do not match, the validation will display an error message
    password_bis = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Form_inscription, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data

def page(request):
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
            return render(request, 'en/public/LOGIN.html', {'form' : form})
    else:
        form = Form_inscription()
    form = Form_inscription()
    return render(request, 'en/public/LOGIN.html', {'form' : form})
