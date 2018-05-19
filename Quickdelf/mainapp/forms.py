from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


# Using Django built in model form creating a form for my models


# Form for user login
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput()) # Password field must not contain a text value. Using PasswordInput

    class Meta:
        model = User
        fields = ('first_name','last_name','username','password','email')


class UseraddnForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields=('DOB','gender','Cardnumber')

# Login page form

class loginForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')


