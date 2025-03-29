from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend ,SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        following_users = user.following.all()  # Assuming a ManyToMany relationship named 'following'
        posts = Post.objects.filter(
            Q(author__in=following_users) | Q(author=user)
        ).order_by('-created_at')  # Assuming 'created_at' is a DateTimeField in Post model
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)