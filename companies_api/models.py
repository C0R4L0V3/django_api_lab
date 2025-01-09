from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30, blank=True)
    industry = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} {self.industry}"
    