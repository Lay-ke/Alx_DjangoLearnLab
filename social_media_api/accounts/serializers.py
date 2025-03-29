from rest_framework import serializers
from .models import CustomUser  # Import your CustomUser model
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser  # Use CustomUser instead of User
        fields = ['username', 'email', 'password', 'password2', 'bio', 'profile_picture']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from validated_data
        password = validated_data.pop('password')  # Get the password
        user = get_user_model().objects.create_user(**validated_data)
        # Set the password (Django will hash it)
        user.set_password(password)
        
        # Save the user
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']
        read_only_fields = ['id', 'username', 'email']


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()

    @staticmethod
    def generate_token(user):
        token = Token.objects.create(user=user)
        return {'token': token.key}
        # token, _ = Token.objects.get_or_create(user=user)
        
