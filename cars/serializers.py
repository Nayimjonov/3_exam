from rest_framework import serializers
from .models import Car


class CarMakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)


class CarModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

class CarFeatureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)



class CarBodyTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class CarListSerializer(serializers.ModelSerializer):
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['make'] = CarMakeSerializer(instance.make).data
        representation['model'] = CarModelSerializer(instance.model).data
        representation['body_type'] = CarBodyTypeSerializer(instance.body_type).data
        return representation


class CarCreateSerializer(serializers.ModelSerializer):
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
            'features',
            'vin',
            'created_at',
            'updated_at'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['make'] = CarMakeSerializer(instance.make).data
        representation['model'] = CarModelSerializer(instance.model).data
        representation['body_type'] = CarBodyTypeSerializer(instance.body_type).data
        representation['features'] = CarFeatureSerializer(instance.features.all(), many=True).data
        return representation


