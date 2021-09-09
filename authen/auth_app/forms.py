from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'phone_number']