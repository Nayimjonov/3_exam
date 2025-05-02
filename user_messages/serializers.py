from rest_framework import serializers


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
    receiver = MessageReceiverSerializer(read_only=True)
    listing = MessageListingSerializer(read_only=True)
    content = serializers.CharField(read_only=True)
    is_read = serializers.BooleanField(read_only=True)


