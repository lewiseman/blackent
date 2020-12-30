from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

 



class RegisterForm(UserCreationForm):
    email =forms.EmailField(help_text='A valid email address, please.')
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):

    class Meta:
        fields = ["username", "password1"]
