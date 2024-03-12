from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from slugify import slugify


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    """Данные о посте"""
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField('Slug', max_length=255, null=True)
    title = models.CharField('Заголовок записи', max_length=100)
    content = models.TextField('Текст записи')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор комментария')
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария', null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
