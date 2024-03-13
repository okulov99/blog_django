from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_list_or_404, render
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Categories
from .forms import AddPostForm, AddCommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator


def index(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def show_categories(request, category_slug=None):

    if category_slug == 'all':
        post = Post.objects.all()
    else:
        post = get_list_or_404(Post.objects.filter(category__slug=category_slug))

    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # paginator = Paginator(post, 3)
    # current_page = paginator.page(int(page))
    # page_obj = paginator.get_page(current_page)
    categories = Categories.objects.all()
    context = {
        'post_list': post,
        'categories': categories,
        'page_obj': page_obj

    }
    return render(request, 'main/main.html', context)


class PostDetail(DetailView):
    """Класс отвечает за отображение страниц с деталями поста"""
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
