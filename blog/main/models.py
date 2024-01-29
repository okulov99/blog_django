from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    """Данные о посте"""
    title = models.CharField('Заголовок записи', max_length=100)
    content = models.TextField('Текст записи')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор комментария')
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
