from django.urls import path
from . import views

urlpatterns = [
    path('asesoria/list/', views.list_asesoria, name='asesoria-list'),
    path('asesoria/new/', views.new_asesoria, name='asesoria-new'),
    # path('asesoria/detail/<int:pk>/', views.detail_asesoria, name='asesoria-detail'),
    # path('asesoria/detail/<int:pk>/', views.detail_asesoria, name='asesoria-detail'),
    path('asesoria/detail/<int:pk>/', views.detail_asesoria, name='asesoria-detail'),
]