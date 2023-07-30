
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from services.models import Service, Review, SubService, Message
from services.serializers.services import ServiceSerializer, ReviewSerializer, SubServiceSerializer, LocationSerializer
from services.serializers.messages import MessageSerializer
from django.contrib.auth.models import User


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


class ReviewsByServiceView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        service_id = self.kwargs['service_id']
        return Review.objects.filter(service_id=service_id)

    def post(self, request, *args, **kwargs):
        service_id = self.kwargs['service_id']
        data = request.data
        if data:
            user = User.objects.get(id=data["user_id"])
            service = Service.objects.get(id=service_id)
            Review.objects.create(
                service=service,
                user=user,
                stars=int(data["stars"]),
                message=data.get("message")
            )
            return Response(status=status.HTTP_201_CREATED)            
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
    
    
class SubServiceListView(APIView):
    def get(self, request, format=None):
        # Get all sub-services from the database
        sub_services = SubService.objects.all()
        
        # Serialize the sub-services data
        serializer = SubServiceSerializer(sub_services, many=True)
        
        # Return the serialized data in the response
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        if data:
            user = User.objects.get(id=data["user_id"])
            Message.objects.create(
                user=user,
                reason=data["reason"],
                message=data["message"]
            )
            return Response(status=status.HTTP_201_CREATED)            
        return Response(status=status.HTTP_400_BAD_REQUEST)