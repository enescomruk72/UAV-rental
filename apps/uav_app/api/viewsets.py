from rest_framework import viewsets

from apps.uav_app.models import Brand, AircraftCategory
from apps.uav_app.api.serializers import BrandSerializer, AircraftCategorySerializer



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class AircraftCategoryViewSet(viewsets.ModelViewSet):
    queryset = AircraftCategory.objects.all()
    serializer_class = AircraftCategorySerializer

