from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>', views.post, name="post"),
    path('profile/', views.profile, name="profile"),
    
    
    # CRUD Paths
    
    path('create_post/', views.createPost, name='create_post'),
    path('updatePost/<slug:slug>/', views.updatePost, name='update_post'),
    path('deletePost/<slug:slug>/', views.deletePost, name='delete_post'),
    
    #Send Email paths
    path('send_email/', views.sendEmail, name='send_email'),
]
