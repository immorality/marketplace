from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomAccountCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = CustomAccountCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'