from django.shortcuts import render

from asesora.models import Asesoria

# Create your views here.
def list_asesoria(request):
    return render(request, 'cliente/list-asesoria.html')

def new_asesoria(request):
    return render(request, 'cliente/new-asesoria.html')

def detail_asesoria(request, pk):
    asesoria = Asesoria.objects.get(pk=pk)
    context = {'asesoria':asesoria}

    return render(request, 'cliente/detail-asesoria.html', context)