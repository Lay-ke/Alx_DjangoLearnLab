from django.urls import path
from .views import list_books, LibraryDetailView, CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('books/', list_books, name='books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail')
]
