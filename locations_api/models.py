from django.db import models

# Create your models here.
class Locations(models.Model):
    address = models.CharField(max_length=30, blank=True)
    city_name = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=28, blank=True)
    country_abbrev = models.CharField(max_length=3, blank=True)


