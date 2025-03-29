from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer, UserProfileSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# User Registration view
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Create a token for the user
            token, _ = Token.objects.get_or_create(user=user)
            # Serialize the user data
            user_data = UserProfileSerializer(user).data
            return Response({
                "message": "User registered successfully.",
                "user": user_data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login view
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"message" : "Login successful.",
                                 "token" : token.key}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Token view
class TokenView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            token_data = TokenSerializer.get_token_for_user(request.user)
            return Response(token_data, status=status.HTTP_200_OK)
        return Response({"error": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
    

# User Profile view
class UserProfileView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            user_data = UserProfileSerializer(user).data
            return Response(user_data, status=status.HTTP_200_OK)
        return Response({"error": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
    

# Follow User view
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        try:
            # Fetch the user by username
            user_to_follow = CustomUser.objects.get(username=username)
            
            # Check if the user is trying to follow themselves
            if user_to_follow == request.user:
                return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

            # Add the user to the following list
            request.user.following.add(user_to_follow)
            return Response({"message": f"You are now following {username}."}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        

# Unfollow User view
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        try:
            # Fetch the user by username
            user_to_unfollow = CustomUser.objects.get(username=username)
            
            # Check if the user is trying to unfollow themselves
            if user_to_unfollow == request.user:
                return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

            # Remove the user from the following list
            request.user.following.remove(user_to_unfollow)
            return Response({"message": f"You have unfollowed {username}."}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


