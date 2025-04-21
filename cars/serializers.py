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


class CarFeatureSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)


class CarSerializer(serializers.ModelSerializer):
    make = CarMakeSerializer()
    model = CarModelSerializer()
    body_type = CarBodyTypeSerializer()
    features = CarFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = (
            'id', 'make', 'model', 'year', 'body_type', 'fuel_type', 'transmission',
            'color', 'mileage', 'engine_size', 'power', 'drive_type', 'vin',
            'created_at', 'updated_at', 'features'
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if hasattr(instance, 'features') and self.context.get('view') and self.context['view'].action == 'create':
            rep['features'] = CarFeatureSerializer(instance.features.all(), many=True).data
        return rep

