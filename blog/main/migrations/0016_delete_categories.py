# Generated by Django 5.0.1 on 2024-03-12 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
    ]