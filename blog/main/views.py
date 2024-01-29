from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Post
from .forms import AddPostForm, AddCommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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
    extra_context = {
        'form': AddCommentForm
    }


class AddPost(LoginRequiredMixin, CreateView):
    """
    Класс отвечает за форму с добавлением постов.
    Страница с формой доступна только для авторизованных пользователей.
    """
    form_class = AddPostForm
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    """Класс отвечает за возможность редактирования существующей записи"""
    model = Post
    fields = ['title', 'content', 'author', 'date', 'img']
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('home')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')


class AddComments(View):
    """Добавление комментариев"""
    def post(self, request, pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.name = request.user
            form.save()
        return redirect(f'/{pk}')
