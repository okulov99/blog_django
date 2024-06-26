from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_list_or_404, render
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Categories
from .forms import AddPostForm, AddCommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from .utils import q_search


def index(request):
    """Главная страница сайта"""
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def show_categories(request, category_slug=None):
    """Отображение статей по выбранным категориям"""
    query = request.GET.get('q', None)
    if category_slug == 'all' or query == '':
        post = Post.objects.all()
    elif query:
        post = q_search(query)
    else:
        post = get_list_or_404(Post.objects.filter(category__slug=category_slug))

    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Categories.objects.all()
    context = {
        'post_list': post,
        'categories': categories,
        'page_obj': page_obj

    }
    return render(request, 'main/main.html', context)


class PostDetail(DetailView):
    """Отображение страниц с деталями поста"""
    model = Post
    template_name = 'main/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
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
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    """Редактирование существующей записи"""
    model = Post
    fields = ['title', 'content', 'author', 'date', 'img']
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('index')


class DeletePost(LoginRequiredMixin, DeleteView):
    """Удаление записи"""
    model = Post
    success_url = reverse_lazy('index')


class AddComments(View):
    """Добавление комментариев"""
    @login_required
    def post(self, request, pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.name = request.user
            form.save()
        return redirect(request.META.get('HTTP_REFERER'))
