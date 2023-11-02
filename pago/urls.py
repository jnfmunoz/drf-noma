from django.urls import path
from . import views

urlpatterns = [
    path('iniciar_pago/<int:factura_id>/', views.iniciar_pago, name='iniciar_pago'),
    path('retorno_pago/<int:factura_id>/', views.retorno_pago, name='retorno_pago'),
]