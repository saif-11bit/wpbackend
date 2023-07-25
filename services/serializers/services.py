
from rest_framework import serializers
from services.models import Service, SubService, Review, Location

class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    sub_services = SubServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
