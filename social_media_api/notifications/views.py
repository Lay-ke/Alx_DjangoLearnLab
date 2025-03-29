from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Notification
from posts.models import Post, Like
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
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
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post).first()
    
    if not like:
        return JsonResponse({'message': 'You have not liked this post.'}, status=400)
    
    like.delete()
    return JsonResponse({'message': 'Post unliked successfully.'})


@login_required
def follow_user(request, user_id):
    followed_user = get_object_or_404(User, id=user_id)
    
    if followed_user == request.user:
        return JsonResponse({'message': 'You cannot follow yourself.'}, status=400)
    
    if request.user.profile.following.filter(id=followed_user.id).exists():
        return JsonResponse({'message': 'You are already following this user.'}, status=400)
    
    request.user.profile.following.add(followed_user)
    
    # Create a notification for the followed user
    Notification.objects.create(
        user=followed_user,
        message=f"{request.user.username} started following you."
    )
    
    return JsonResponse({'message': 'User followed successfully.'})


@login_required
def comment_on_post(request, post_id):

    @method_decorator(csrf_exempt, name='dispatch')
    def post_comment(request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                comment_text = data.get('comment', '').strip()
                if not comment_text:
                    return JsonResponse({'message': 'Comment cannot be empty.'}, status=400)
                
                post = get_object_or_404(Post, id=post_id)
                comment = post.comments.create(user=request.user, text=comment_text)
                
                # Create a notification for the post owner
                if post.author != request.user:
                    Notification.objects.create(
                        user=post.author,
                        message=f"{request.user.username} commented on your post: {comment_text}"
                    )
                
                return JsonResponse({'message': 'Comment added successfully.', 'comment': comment.text})
            except json.JSONDecodeError:
                return JsonResponse({'message': 'Invalid JSON data.'}, status=400)
        return JsonResponse({'message': 'Invalid request method.'}, status=405)
    

@login_required
def fetch_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    unread_notifications = notifications.filter(is_read=False)
    
    response_data = {
        'unread_notifications': [
            {'id': n.id, 'message': n.message, 'created_at': n.created_at} for n in unread_notifications
        ],
        'all_notifications': [
            {'id': n.id, 'message': n.message, 'created_at': n.created_at, 'is_read': n.is_read} for n in notifications
        ]
    }
    
    return JsonResponse(response_data)