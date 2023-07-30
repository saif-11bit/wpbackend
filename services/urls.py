from django.urls import path
from services.views.authen import CustomTokenObtainPairView, CustomTokenRefreshView, LogoutView
from services.views.register import register_user
from services.views.services import AllServiceView, SubServiceByServiceView, ReviewsByServiceView, ServiceDetailsView, SubServiceListView, MessageView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register'),
    path('services/', AllServiceView.as_view(), name='all-services'),
    path('message/', MessageView.as_view(), name='send-message'),
    path('subservices/', SubServiceListView.as_view(), name='all-sub-services'),
    path('services/<int:service_id>/', ServiceDetailsView.as_view(), name='service-details'),
    path('services/<int:service_id>/subservices/', SubServiceByServiceView.as_view(), name='subservices-by-service'),
    path('services/<int:service_id>/reviews/', ReviewsByServiceView.as_view(), name='reviews-by-service'),

]