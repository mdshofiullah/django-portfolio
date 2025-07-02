from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('profile/', views.profile, name="profile"),

    # CRUD paths
    path('create-post/', views.createPost, name='create_post'),
    path('update-post/<slug:slug>/', views.updatePost, name='update_post'),
    path('delete-post/<slug:slug>/', views.deletePost, name='delete_post'),

    # Send email path
    path('send-email/', views.sendEmail, name='send_email'),
]
