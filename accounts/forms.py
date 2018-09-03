from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class AccountCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'password', 'seller')

class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email')