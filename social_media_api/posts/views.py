from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from notifications.models import Notification

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
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Assuming 'created_at' is a DateTimeField in Post model
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
# Like post
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        return JsonResponse({'message': 'You have already liked this post.'}, status=400)
    
    # Create a notification for the post owner
    if post.author != request.user:
        Notification.objects.create(
            user=post.author,
            message=f"{request.user.username} liked your post."
        )
    
    return JsonResponse({'message': 'Post liked successfully.'})

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    like = Like.objects.filter(user=request.user, post=post).first()
    
    if not like:
        return JsonResponse({'message': 'You have not liked this post.'}, status=400)
    
    like.delete()
    return JsonResponse({'message': 'Post unliked successfully.'})
