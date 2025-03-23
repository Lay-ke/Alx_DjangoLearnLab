from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='blog-login'),
    path('register/', views.register, name='blog-register'),
    path('profile/', views.profile, name='blog-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='blog-logout'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]