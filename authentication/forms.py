from django import forms

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

