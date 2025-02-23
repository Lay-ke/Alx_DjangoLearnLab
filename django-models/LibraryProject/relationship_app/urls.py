from django.urls import path
from .views import list_books, LibraryDetailView, UserRegisterView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('books/', list_books, name='books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail')
]
