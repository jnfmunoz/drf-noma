from django.urls import path
from .views import RegionComunaListCreateView

urlpatterns = [
    path('regiones-comunas/', RegionComunaListCreateView.as_view(), name='region_comuna_list_create-comunas'),   
]