# INF601 - Advanced Programming in Python
# Iris Perry
# Mini Project 4

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Habit

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name']