from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView

from apps.uav_app.models import Brand, AircraftCategory, ContactMessage
from apps.uav_app.api.serializers import BrandSerializer, AircraftCategorySerializer, ContactMessageSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class AircraftCategoryViewSet(viewsets.ModelViewSet):
    queryset = AircraftCategory.objects.all()
    serializer_class = AircraftCategorySerializer



class ContactMessageViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = ContactMessageSerializer

    def get_queryset(self):
        # Mevcut kullanıcıya ait mesajları döndür
        return ContactMessage.objects.filter(user=self.request.user)

    