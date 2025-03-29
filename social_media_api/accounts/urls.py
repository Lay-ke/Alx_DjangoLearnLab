from django.urls import path
from .views import UserRegistrationView, UserLoginView, TokenView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/', TokenView.as_view(), name='token'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]