from rest_framework import serializers
from accounts.models import CustomUser
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', queryset=CustomUser.objects.all(), write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author', queryset=CustomUser.objects.all(), write_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'author_id', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_content(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Content must be at least 3 characters long.")
        return value