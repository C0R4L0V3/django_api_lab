from django.urls import path
from . import views

urlpatterns = [
    path('api/locations', views.LocationsList.as_view(), name='locations_list'),
    path('api/locations/<int:pk>', views.LocationsDetail.as_view(), name='locations_detail'),
]


