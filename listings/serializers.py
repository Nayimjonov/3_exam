from rest_framework import serializers
from .models import Listing


class ListingCarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    make = serializers.CharField(read_only=True)
    model = serializers.CharField(read_only=True)
    year = serializers.DateField(read_only=True)
    body_type = serializers.CharField(read_only=True)


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            'id',
            'title',
            'description',
            'price',
            'currency',
            'location',
            'condition',
            'is_negotiable',
            'is_active',
            'views_count',
            'created_at',
            'updated_at',
            'expires_at',
            'car',
            'seller',
            'primary_image',
            'images_count'
        )
