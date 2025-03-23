from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='blog-login'),
    path('register/', views.register, name='blog-register'),
    path('profile/', views.profile, name='blog-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='blog-logout'),
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<slug:tag_slug>/', views.PostsByTagListView.as_view(), name='posts-by-tag'),
    path('search/', views.PostSearchView.as_view(), name='search-results'),
]