from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'date', 'img']
