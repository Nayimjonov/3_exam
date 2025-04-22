from rest_framework import serializers
from .models import Listing


class ListingCarMakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ListingCarModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ListingCarBodyTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ListingCarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    make = ListingCarMakeSerializer(read_only=True)
    model = ListingCarModelSerializer(read_only=True)
    year = serializers.IntegerField(read_only=True)
    body_type = ListingCarBodyTypeSerializer(read_only=True)
    fuel_type = serializers.CharField(read_only=True)
    transmission = serializers.CharField(read_only=True)
    color = serializers.CharField(read_only=True)
    mileage = serializers.CharField(read_only=True)

class ListingSellerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    user_type = serializers.CharField(read_only=True)

class ListingSerializer(serializers.ModelSerializer):
    images_count = serializers.SerializerMethodField()

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

    def get_images_count(self, obj):
        return 1 if obj.primary_image else 0

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['car'] = ListingCarSerializer(instance.car).data
        representation['seller'] = ListingSellerSerializer(instance.seller).data
        return representation

