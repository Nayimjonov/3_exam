from rest_framework import serializers
from .models import Make


class MakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    logo = serializers.ImageField(read_only=True)



