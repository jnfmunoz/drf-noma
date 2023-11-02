from django.urls import path, include

from .views import (AsesoriaListAV, AsesoriaCreateAV, AsesoriaDetailAV, AsesoriaUpdateAV, 
                    AccidenteListAV, AccidenteCreateAV,AccidenteDetailAV, AccidenteUpdateAV,
                    CapacitacionListAV, CapacitacionDetailAV, ContratoListAV, ContratoDetailAV,
                    VisitaListAV, VisitaDetailAV, FacturaListAV, FacturaDetailAV, FormularioVisitaAV,
                    DetalleFormularioAV)

urlpatterns = [
    
    # ASESORIAS 
    path('asesoria/list/', AsesoriaListAV.as_view(), name='list-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/asesoria/list/
    path('asesoria/new/', AsesoriaCreateAV.as_view(), name='new-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/asesoria/new/
    path('asesoria/detail/<int:pk>/', AsesoriaDetailAV.as_view(), name='detail-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/asesoria/detail/<int:pk>/
    path('asesoria/update/<int:pk>/', AsesoriaUpdateAV.as_view(), name='update-asesoria-cliente-api'), # http://127.0.0.1:8000/cliente-api/asesoria/update/<int:pk>/
    
    # ACCIDENTES
    path('accidente/list/', AccidenteListAV.as_view(), name='list-accidente-cliente-api'), # http://127.0.0.1:8000/cliente-api/accidente/list/
    path('accidente/new/', AccidenteCreateAV.as_view(), name='new-accidente-cliente-api'), # http://127.0.0.1:8000/cliente-api/accidente/new/
    path('accidente/detail/<int:pk>/', AccidenteDetailAV.as_view(), name='detail-accidente-cliente-api'), # http://127.0.0.1:8000/cliente-api/accidente/detail/<int:pk>/
    path('accidente/update/<int:pk>/', AccidenteUpdateAV.as_view(), name='update-accidente-cliente-api'), # http://127.0.0.1:8000/cliente-api/accidente/update/<int:pk>/

    # CAPACITACIONES 
    path('capacitacion/list/', CapacitacionListAV.as_view(), name='list-capacitacion-cliente-api'), # http://127.0.0.1:8000/cliente-api/capacitacion/list/
    path('capacitacion/detail/<int:pk>/', CapacitacionDetailAV.as_view(), name='detail-capacitacion-cliente-api'), # http://127.0.0.1:8000/cliente-api/capacitacion/detail/<int:pk>/

    # VISITAS
    path('visita/list/', VisitaListAV.as_view(), name='list-visita-cliente-api'), # http://127.0.0.1:8000/cliente-api/visita/list/
    path('visita/detail/<int:pk>/', VisitaDetailAV.as_view(), name='detail-visita-cliente-api'), # http://127.0.0.1:8000/cliente-api/visita/detail/<int:pk>/

    # FACTURAS
    path('factura/list/', FacturaListAV.as_view(), name='list-factura-cliente-api'), # http://127.0.0.1:8000/cliente-api/factura/list/
    path('factura/detail/<int:pk>/', FacturaDetailAV.as_view(), name='detail-factura-cliente-api'), # http://127.0.0.1:8000/cliente-api/factura/detail/<int:pk>/

    # CONTRATO
    path('contrato/list/', ContratoListAV.as_view(), name='list-contrato-cliente-api'), # http://127.0.0.1:8000/cliente-api/contrato/list/
    path('contrato/detail/<int:pk>/', ContratoDetailAV.as_view(), name='detail-contrato-cliente-api'), # http://127.0.0.1:8000/cliente-api/contrato/detail/<int:pk>/

    # FORMULARIO VISITA
    path('formulario/list/', FormularioVisitaAV.as_view(), name="formulario-visita-cliente-api"), # http://127.0.0.1:8000/cliente-api/formulario/list/
    
    # ELEMENTO REVISION
    path('detalle-formulario/list/', DetalleFormularioAV.as_view(), name="detalle-formulario-cliente-api") # http://127.0.0.1:8000/cliente-api/detalle-formulario/list/
]