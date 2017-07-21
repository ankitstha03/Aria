from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	first_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	last_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
	email= forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    
	class Meta:
		model = User
		fields = ['first_name', 'last_name','username', 'email', 'password']
