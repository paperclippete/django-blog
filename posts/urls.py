from django.urls import path
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    path('', get_posts, name="get_posts"),
    path('detail/<pk>/', post_detail, name="post_detail"),
    path('new/', create_or_edit_post, name="new_post"),
    path('edit/<pk>/', create_or_edit_post, name="edit_post")
    ]