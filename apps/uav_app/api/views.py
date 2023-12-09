from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

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


class RentalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    
