from django.urls import path
from . import views


urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('add_post/', views.AddPost.as_view(), name='add_post'),
     path('<int:pk>/', views.PostDetail.as_view())
]