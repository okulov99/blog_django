from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


