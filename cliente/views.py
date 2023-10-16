from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from asesora.models import Asesoria
# Create your views here.
def list_asesoria(request):
    return render(request, 'cliente/list-asesoria.html')

def new_asesoria(request):
    return render(request, 'cliente/new-asesoria.html')

