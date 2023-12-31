from django.urls import path
from . import views

urlpatterns = [
    # ASESORIAS
    path('asesoria/list/', views.list_asesoria, name='asesoria-list'),
    path('asesoria/new/', views.new_asesoria, name='asesoria-new'),
    path('asesoria/detail/<int:pk>/', views.detail_asesoria, name='asesoria-detail'),
    path('asesoria/update/<int:pk>/', views.update_asesoria, name='asesoria-update'),

    # ACCIDENTES
    path('accidente/list/', views.list_accidente, name='accidente-list'),
    path('accidente/new/', views.new_accidente, name='accidente-new'),
    path('accidente/detail/<int:pk>/', views.detail_accidente, name='accidente-detail'),
    path('accidente/update/<int:pk>/', views.update_accidente, name='asesoria-update'),

    # CAPACITACIONES
    path('capacitacion/list/', views.list_capacitacion, name='capacitacion-list'),
    path('capacitacion/detail/<int:pk>/', views.detail_capacitacion, name='capacitacion-detail'),

    # CONTRATOS
    path('contrato/list/', views.list_contrato, name='contrato-list'),
    path('contrato/detail/<int:pk>/', views.detail_contrato, name='contrato-detail'),

    # VISITAS
    path('visita/list/', views.list_visita, name='visita-list'),
    path('visita/detail/<int:pk>/', views.detail_visita, name='visita-detail'),

    # FACTURAS 
    path('factura/list/', views.list_factura, name='factura-list'),
    path('factura/detail/<int:pk>/', views.detail_factura, name='factura-detail'),

    path('paypal-return/', views.paypal_return, name='paypal-return'),
    path('paypal-cancel/', views.paypal_cancel, name='paypal-cancel'),

    # FORMULARIO VISITA
    path('formulario-visita/list/', views.list_item, name='formulario-visita'),

]