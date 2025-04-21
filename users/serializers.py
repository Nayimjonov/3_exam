from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile
from rest_framework.authtoken.models import Token


User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'user_type', 'phone', 'avatar', 'location', 'rating', 'created_at')
        read_only_fields = ('id', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile']


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=UserProfile.CHOICES_USER_TYPE, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'user_type',
            'token'
        )
        read_only_fields = ('id', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password_confirm')
        user_type = validated_data.pop('user_type')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(
            user=user,
            user_type=user_type,
            phone='',
            avatar=None,
            location='',
            rating=0
        )
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data['user_type'] = instance.profile.user_type
        except:
            data['user_type'] = None
        return data





