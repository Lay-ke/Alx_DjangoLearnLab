from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Model representing a post in the application.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """
    Model representing a comment on a post.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'