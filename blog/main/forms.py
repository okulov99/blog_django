import datetime
from django import forms
from django.utils.text import slugify

from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    this_year = datetime.date.today().year
    date = forms.DateField(initial=datetime.date.today,
                                 label='Дата публикации', disabled=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'img']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
