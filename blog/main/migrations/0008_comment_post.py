# Generated by Django 5.0.1 on 2024-01-29 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment_delete_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.post', verbose_name='Публикация'),
            preserve_default=False,
        ),
    ]
