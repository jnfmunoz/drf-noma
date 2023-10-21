from django.shortcuts import render

from asesora.models import Asesoria, Accidente

# Create your views here.
def list_asesoria(request):
    return render(request, 'cliente/asesoria/list-asesoria.html')

def new_asesoria(request):
    return render(request, 'cliente/asesoria/new-asesoria.html')

def detail_asesoria(request, pk):
    asesoria = Asesoria.objects.get(pk=pk)
    context = {'asesoria':asesoria}

    return render(request, 'cliente/asesoria/detail-asesoria.html', context)

def update_asesoria(request, pk):
    asesoria = Asesoria.objects.get(pk=pk)
    context = {'asesoria':asesoria}

    return render(request, 'cliente/asesoria/update-asesoria.html', context)

def list_accidente(request):
    return render(request, 'cliente/accidente/list-accidente.html')

def new_accidente(request):
    return render(request, 'cliente/accidente/new-accidente.html')

def detail_accidente(request, pk):
    accidente = Accidente.objects.get(pk=pk)
    context = {'accidente':accidente}

    return render(request, 'cliente/accidente/detail-accidente.html', context)

def update_accidente(request, pk):
    accidente = Accidente.objects.get(pk=pk)
    context = {'accidente':accidente}

    return render(request, 'cliente/accidente/update-accidente.html', context)
