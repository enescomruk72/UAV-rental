
from rest_framework import generics

from apps.uav_app.api.serializers import UCAVSerializer, RentalSerializer
from apps.uav_app.models import UCAV, Rental



class UCAVListCreateAPIView(generics.ListCreateAPIView):
    queryset = UCAV.objects.all()
    serializer_class = UCAVSerializer


class UCAVDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UCAV.objects.all()
    serializer_class = UCAVSerializer


    
class RentalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        # Yalnızca istek yapan kullanıcıya ait kiralama kayıtlarını döndür
        return Rental.objects.filter(user=self.request.user)


class RentalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        # Yalnızca istek yapan kullanıcıya ait kiralama kayıtlarını döndür
        return Rental.objects.filter(user=self.request.user)
