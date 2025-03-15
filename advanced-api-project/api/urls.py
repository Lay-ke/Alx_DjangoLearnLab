from django.urls import path
from .views import CreateView, DeleteView, UpdateView, DetailView, ListView

urlpatterns = [
    path('books/create/', CreateView.as_view(), name='create'),
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('books/<int:pk>/', DetailView.as_view(), name='detail'),
    path('books/', ListView.as_view(), name='list'),
]