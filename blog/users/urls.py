from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]


# {% if user.is_authenticated %}
#     <li class="last"> {{user.username}} | <a href="{% url 'users:logout' %}">Выйти</a></li>
# {% else %}
#     <li class="last"><a href="{% url 'users:login' %}">Войти</a> | <a href="#">Регистрация</a></li>
# {% endif %}