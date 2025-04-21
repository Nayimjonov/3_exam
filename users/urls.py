from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path('auth/register/', views.UserCreateView.as_view(), name='register'),
    path('auth/login/', views.CustomTokenObtainPairView.as_view(), name='user-login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('auth/logout/', views.UserLogoutView.as_view(), name='user-logout'),

]