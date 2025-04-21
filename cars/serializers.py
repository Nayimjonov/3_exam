from rest_framework import serializers
from .models import Car




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



