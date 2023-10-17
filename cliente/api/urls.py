from django.urls import path, include

from .views import AsesoriaListAV, AsesoriaCreateAV, AsesoriaDetailAV

urlpatterns = [
    
    # ASESORIAS 
    path('asesoria/list/', AsesoriaListAV.as_view(), name='list-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/asesoria/list/
    path('asesoria/new/', AsesoriaCreateAV.as_view(), name='new-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/asesoria/new/
    path('asesoria/detail/<int:pk>/', AsesoriaDetailAV.as_view(), name='detail-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/asesoria/detail/<int:pk>/
    
]