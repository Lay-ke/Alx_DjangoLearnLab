from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_all_books, name='books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail')
]
