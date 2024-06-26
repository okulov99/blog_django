# Generated by Django 5.0.1 on 2024-01-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]
