from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile


User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    user_type = serializers.CharField()
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_type = serializers.ChoiceField(choices=UserProfile.CHOICES_USER_TYPE)
    phone = serializers.CharField(max_length=13)
    avatar = serializers.ImageField()
    location = serializers.CharField(max_length=255)
    rating = serializers.FloatField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.location = validated_data.get('location', instance.location)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance