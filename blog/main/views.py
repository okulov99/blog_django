#from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView


class Home(ListView):
    model = Post
    template_name = 'main/main.html'
    context_object_name = 'post_list'


class PostDetail(DetailView):
    model = Post
    template_name = 'main/post_detail.html'
    context_object_name = 'post'


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('home')

