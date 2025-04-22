from rest_framework import serializers
from .models import Listing




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
