from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_asesoria, name='asesoria-list'),
    path('new/', views.new_asesoria, name='asesoria-new'),
]