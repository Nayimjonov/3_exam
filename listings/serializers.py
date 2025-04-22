from rest_framework import serializers
from datetime import timedelta
from django.utils import timezone
from .models import Listing, Car


class ListingCarMakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ListingCarModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ListingCarBodyTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ListingCarReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    make = ListingCarMakeSerializer(read_only=True)
    model = ListingCarModelSerializer(read_only=True)
    year = serializers.IntegerField(read_only=True)
    body_type = ListingCarBodyTypeSerializer(read_only=True)
    fuel_type = serializers.CharField(read_only=True)
    transmission = serializers.CharField(read_only=True)
    color = serializers.CharField(read_only=True)
    mileage = serializers.IntegerField(read_only=True)


class ListingSellerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    user_type = serializers.CharField(read_only=True)


class ListingSerializer(serializers.ModelSerializer):
    images_count = serializers.SerializerMethodField()
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), write_only=True)
    seller = ListingSellerSerializer(read_only=True)
    primary_image = serializers.ImageField(required=False, allow_null=True)
    expires_at = serializers.DateTimeField(read_only=True)

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
            'is_featured',
            'views_count',
            'created_at',
            'updated_at',
            'expires_at',
            'car',
            'seller',
            'primary_image',
            'images_count',
        )

    def get_images_count(self, obj):
        return 1 if obj.primary_image else 0

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['car'] = ListingCarReadSerializer(instance.car).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['seller'] = request.user

        validated_data['expires_at'] = timezone.now() + timedelta(days=90)
        return super().create(validated_data)


# DETAIL
class ListingCarDetailMakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)

class ListingCarDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    make = ListingCarDetailMakeSerializer(read_only=True)
    model = ListingCarModelSerializer(read_only=True)
    year = serializers.IntegerField(read_only=True)
    body_type = ListingCarBodyTypeSerializer(read_only=True)



class ListingDetailSerializer(serializers.ModelSerializer):
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
            'is_featured',
            'views_count',
            'created_at',
            'updated_at',
            'expires_at',
            'car',
            'fuel_type',
            'transmission',
            'color',
            'mileage',
            'engine_size',
            'power',
            'drive_type',
            'features',
            'seller',
            'images',
            'similar_listings'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['car'] = ListingCarDetailSerializer(instance.car).data
        return representation