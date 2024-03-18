from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from main.models import Post


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    extra_context = {
        'default_image': settings.DEFAULT_USER_IMAGE,
    }


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'users/password_change_form.html'


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))
