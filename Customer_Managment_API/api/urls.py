from django.urls import path, include
from .views import (CustomerModelViewSet,
                    OrderModelViewSet,
                    UserRegistrationView)

from rest_framework.routers import DefaultRouter
    
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'customers', CustomerModelViewSet, basename='customer')
router.register(r'orders', OrderModelViewSet, basename='order')


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]