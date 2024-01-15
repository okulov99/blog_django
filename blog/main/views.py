from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm


def show_main(request):
    posts = Post.objects.all()
    return render(request, 'main/main.html', {'post_list': posts})


def add_post(request):
    form = AddPostForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('home')
    return render(request, 'main/add_post.html', {'form': form})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'main/post_detail.html', {'post': post})
