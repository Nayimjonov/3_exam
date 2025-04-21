from rest_framework import serializers
from .models import Make, Model


class MakeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    logo = serializers.ImageField(read_only=True)


class ModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    make = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())

    def create(self, validated_data):
        return Model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.make = validated_data.get('make', instance.make)
        instance.save()
        return instance

