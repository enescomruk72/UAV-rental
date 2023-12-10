from django.urls import path, include
from rest_framework.routers import DefaultRouter


from apps.uav_app.api.viewsets import BrandViewSet, AircraftCategoryViewSet
from apps.uav_app.api.views import (
    UCAVListCreateAPIView,
    UCAVDetailAPIView,
    RentalListCreateAPIView,
    RentalDetailAPIView
)

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'aircraft-categories', AircraftCategoryViewSet)

urlpatterns = [
    # Brands - AircraftCategory
    path('', include(router.urls)),

    path('ucavs/', UCAVListCreateAPIView.as_view(), name='ucav-list&create'),
    path('ucavs/<int:pk>/', UCAVDetailAPIView.as_view(), name='ucav-detail'),
    path('rentals/', RentalListCreateAPIView.as_view(), name='rental-list&create'),
    path('rentals/<int:pk>/', RentalDetailAPIView.as_view(), name='rental-detail'),
   
]
