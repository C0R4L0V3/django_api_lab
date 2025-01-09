from django.shortcuts import render
from rest_framework import generics
from .serializers import LocationsSerializer
from .models import Locations

# Create your views here.
class LocationsList(generics.ListCreateAPIView):
    queryset = Locations.objects.all().order_by('id')
    serializer_class = LocationsSerializer

class LocationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locations.objects.all().order_by('id')
    serializer_class = LocationsSerializer
