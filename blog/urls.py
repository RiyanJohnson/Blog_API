from django.urls import path
from .views import get_post,create_post,post_detail,delete_post

urlpatterns=[
    path('posts/',get_post, name = 'get_post'),
    path('create/',create_post, name = 'create_post'),
    path('posts/<int:pk>',post_detail,name = 'post_detail'),
    path('posts/<int:pk>/delete',delete_post,name = 'delete-post'),
]