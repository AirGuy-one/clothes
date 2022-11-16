from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Введите логин', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 280px;'}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width: 280px;'}))

