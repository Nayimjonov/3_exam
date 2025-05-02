from django.urls import path
from . import views


urlpatterns = [
    path('messages/', views.MessageListCreateView.as_view(), name='message-list'),
]