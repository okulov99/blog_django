from django.urls import path
from . import views


urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('add_post/', views.AddPost.as_view(), name='add_post'),
     path('post/<slug:post_slug>/', views.PostDetail.as_view(), name='post'),
     path('edit/<int:pk>/', views.UpdatePost.as_view(), name='edit_page'),
     path('delete/<int:pk>', views.DeletePost.as_view(), name='del_page'),
     path('review/<int:pk>/', views.AddComments.as_view(), name="add_comments")
]
