from django.db import models

# Create your models here.
class Locations(models.Model):
    address = models.CharField(max_length=30, blank=True)
    city_name = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=28, blank=True)
    country_abbrev = models.CharField(max_length=3, blank=True)
    company = models.ForeignKey(
        'companies_api.Company', #this should refrence the companies_api
        on_delete=models.CASCADE, # delete the location if the company is deleted
        related_name='locations'  # allows to reverse lookup: company.locations.all()

    )

    def __str__(self):
        return f"{self.city_name} {self.zip_code} {self.state} {self.country} {self.country_abbrev}"


