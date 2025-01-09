from rest_framework import serializers
from .models import Locations

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('id', 'address', 'city_name', 'state', 'zip_code', 'country', 'country_abbrev',)
