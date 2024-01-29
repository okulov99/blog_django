from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'img']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
