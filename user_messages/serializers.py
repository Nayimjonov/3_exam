from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User
from listings.models import Listing


class MessageSenderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class MessageReceiverSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class MessageListingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)


class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender = MessageSenderSerializer(read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    receiver_detail = MessageReceiverSerializer(source='receiver', read_only=True)
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all(), write_only=True)
    listing_detail = MessageListingSerializer(source='listing', read_only=True)
    content = serializers.CharField()
    is_read = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['sender'] = request.user if request and hasattr(request, 'user') else None

        return Message.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.is_read = validated_data.get('is_read', instance.is_read)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['receiver'] = representation.pop('receiver_detail')
        representation['listing'] = representation.pop('listing_detail')
        return representation