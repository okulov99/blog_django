import datetime
from django import forms
from django.utils.text import slugify

from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    this_year = datetime.date.today().year
    date = forms.DateField(initial=datetime.date.today,
                                 label='Дата публикации', disabled=True)
    title = forms.CharField(label='Заголовок записи', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст записи', widget=forms.Textarea(attrs={'class': 'form-control'}))
    img = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'date', 'img', 'category']


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
