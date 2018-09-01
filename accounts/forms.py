from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomAccount

class CustomAccountCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomAccount
        fields = ('username', 'email','is_seller')

class CustomAccountChangeForm(UserChangeForm):

    class Meta:
        model = CustomAccount
        fields = ('username', 'email', 'is_seller')