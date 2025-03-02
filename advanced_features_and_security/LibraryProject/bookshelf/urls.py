from django.urls import path
from . import views

urlpatterns = [
    path('book/all/', views.book_list, name='book_lists'),  # List of all books
    path('book/<int:book_id>/', views.view_book, name='book_detail'),  # View a single book
    path('book/create/', views.create_book, name='create_a_book'),  # Create a new book
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_a_book'),  # Edit a book
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_a_book'),  # Delete a book
]
