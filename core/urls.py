"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # cliente 
    path('cliente/', include('cliente.urls')), # # http://127.0.0.1:8000/cliente/

    # cliente-api
    path('cliente-api/', include('cliente.api.urls')), # http://127.0.0.1:8000/cliente-api/
    # asesora-api
    path('asesora-api/', include('asesora.api.urls')), # http://127.0.0.1:8000/asesora-api/

    # registration-api
    path('registration-api/', include('registration.api.urls')), # http://127.0.0.1:8000/registration-api/

    # path de auth
    path('accounts/', include('django.contrib.auth.urls')),

    # temporary login and logout api 
    path('api-auth/', include('rest_framework.urls')), 
]
