from rest_framework import serializers
from .models import Dealer
from reviews.models import Review


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
class CarMakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class CarModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    make = CarMakeSerializer(read_only=True)
    model = CarModelSerializer(read_only=True)
    year = serializers.IntegerField()


class ListingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField(max_length=3)
    location = serializers.CharField(max_length=100)
    condition = serializers.CharField(max_length=10)
    is_negotiable = serializers.BooleanField()
    is_active = serializers.BooleanField()
    is_featured = serializers.BooleanField()
    views_count = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    car = CarSerializer()
    primary_image = serializers.SerializerMethodField()

    def get_primary_image(self, obj):
        return obj.primary_image.url if obj.primary_image else None

# dealer/<id>/reviews/
class ReviewUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)


class DealerReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    reviewer = ReviewUserSerializer(read_only=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        dealer = self.context['dealer']
        user = self.context['request'].user

        if not user.is_authenticated:
            raise serializers.ValidationError("Authentication required to create a review")

        from listings.models import Listing
        default_listing = Listing.objects.first()  # Get the first listing or create one
        if not default_listing:
            default_listing = Listing.objects.create(
                title="Default Listing",
                seller=dealer.user,
            )

        review = Review(
            reviewer=user,
            reviewed_user=dealer.user,
            listing=default_listing,
            rating=validated_data['rating'],
            comment=validated_data['comment']
        )
        review.save()
        return review

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance