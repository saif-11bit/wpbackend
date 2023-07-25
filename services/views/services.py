
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.models import Service, Review
from services.serializers.services import ServiceSerializer, ReviewSerializer, SubServiceSerializer, LocationSerializer


class AllServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubServiceByServiceView(APIView):
    def get(self, request, service_id):
        try:
            service = Service.objects.get(pk=service_id)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
        
        sub_services = service.sub_services.all()
        serializer = SubServiceSerializer(sub_services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReviewsByServiceView(APIView):
    def get(self, request, service_id):
        try:
            service = Service.objects.get(pk=service_id)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
        
        reviews = Review.objects.filter(service=service)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceDetailsView(APIView):
    def get(self, request, service_id):
        try:
            service = Service.objects.get(pk=service_id)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the service details
        service_serializer = ServiceSerializer(service)

        # Serialize the associated reviews and locations
        reviews_serializer = ReviewSerializer(service.review_set.all(), many=True)
        locations_serializer = LocationSerializer(service.locations.all(), many=True)

        # Combine the data and return as a JSON response
        response_data = {
            "service": service_serializer.data,
            "reviews": reviews_serializer.data,
            "locations": locations_serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)