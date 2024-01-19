from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView


class Home(ListView):
    """Класс отвечает за отображение главной страницы сайта"""
    model = Post
    template_name = 'main/main.html'
    context_object_name = 'post_list'
    paginate_by = 3


class PostDetail(DetailView):
    """Класс отвечает за отображение страниц с деталями поста"""
    model = Post
    template_name = 'main/post_detail.html'
    context_object_name = 'post'


class AddPost(LoginRequiredMixin, CreateView):
    """
    Класс отвечает за форму с добавлением постов.
    Страница с формой доступна только для авторизованных пользователей.
    """
    form_class = AddPostForm
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('home')

