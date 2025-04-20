from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from users.serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        data = response.data
        data['user'] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_type": user.profile.user_type if hasattr(user, 'profile') else None,
        }
        return Response(data)