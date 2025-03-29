from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.fetch_notifications, name='notifications_list'),
]