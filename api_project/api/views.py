from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics

# Create your views here.
class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
