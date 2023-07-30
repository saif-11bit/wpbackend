
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
    username = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'username', 'stars', 'message']

    def get_username(self, obj):
        return obj.user.username


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ['id', 'sub_service_name', 'starting_price']