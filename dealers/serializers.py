from rest_framework import serializers
from .models import Dealer


class DealerUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)



class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = (
            'id',
            'user',
            'company_name',
            'description',
            'logo',
            'website',
            'address',
            'is_verified',
            'rating',
            'created_at',
            'updated_at'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = DealerUserSerializer(instance.user).data
        return representation


class DealerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = (
            'company_name', 'description', 'logo',
            'website', 'address'
        )
        read_only_fields = ('logo',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Dealer.objects.create(user=user, **validated_data)

# dealer/<id>/listing
class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    make = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    year = serializers.IntegerField()

class ListingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField(max_length=10)
    location = serializers.CharField(max_length=100)
    condition = serializers.CharField(max_length=50)
    is_negotiable = serializers.BooleanField()
    is_active = serializers.BooleanField()
    is_featured = serializers.BooleanField()
    views_count = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    car = CarSerializer()
    primary_image = serializers.ImageField()

class DealerListingSerializer(serializers.Serializer):
    user = serializers.StringRelatedField()
    company_name = serializers.CharField(max_length=200)
    description = serializers.CharField()
    logo = serializers.ImageField()
    website = serializers.URLField()
    address = serializers.CharField()
    is_verified = serializers.BooleanField()
    rating = serializers.FloatField()
    listings = ListingSerializer(many=True)

