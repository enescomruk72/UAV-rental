
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.uav_app.api.serializers import UCAVSerializer, RentalSerializer
from apps.uav_app.models import UCAV, Rental



class UCAVListCreateAPIView(generics.ListCreateAPIView):
    queryset = UCAV.objects.all()
    serializer_class = UCAVSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class UCAVDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UCAV.objects.all()
    serializer_class = UCAVSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    
class RentalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    filterset_fields = ('ucav__name', 'ucav__model')

    def get_queryset(self):
        # Yalnızca istek yapan kullanıcıya ait kiralama kayıtlarını döndür
        return Rental.objects.filter(user=self.request.user)


class RentalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        # Yalnızca istek yapan kullanıcıya ait kiralama kayıtlarını döndür
        return Rental.objects.filter(user=self.request.user)
