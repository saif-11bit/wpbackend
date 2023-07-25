from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

class CustomTokenObtainPairView(TokenObtainPairView):
    # Customize the response if needed
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Add custom data to the response if needed
        return response

class CustomTokenRefreshView(TokenRefreshView):
    # Customize the response if needed
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Add custom data to the response if needed
        return response

@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def post(self, request):
        # Perform logout actions if needed
        return Response({"detail": "Logout successful"})
