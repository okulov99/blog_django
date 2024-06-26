# Generated by Django 5.0.1 on 2024-01-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок записи')),
                ('content', models.TextField(verbose_name='Текст записи')),
                ('author', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('date', models.DateField(verbose_name='Дата публикации')),
                ('img', models.ImageField(upload_to='image/%Y', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
