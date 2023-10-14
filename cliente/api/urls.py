from django.urls import path, include

from .views import AsesoriaListAV, AsesoriaCreateAV

urlpatterns = [
    path('list-asesoria-cliente-api/', AsesoriaListAV.as_view(), name='list-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/list-asesoria-cliente-api/
    path('new-asesoria-cliente-api/', AsesoriaCreateAV.as_view(), name='new-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/new-asesoria-cliente-api/
    
]