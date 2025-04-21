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


