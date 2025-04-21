from rest_framework import serializers
from .models import Car


class CarMakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)


class CarModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class CarBodyTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'make',
            'model',
            'year',
            'body_type',
            'fuel_type',
            'transmission',
            'color',
            'mileage',
            'engine_size',
            'power',
            'drive_type',
            'vin',
            'created_at',
            'updated_at'
        )



