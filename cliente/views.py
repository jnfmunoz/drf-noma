from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

from asesora.models import Asesoria, Accidente, Capacitacion, Contrato, Visita, Factura

# Create your views here.
def list_asesoria(request):
    return render(request, 'cliente/asesoria/list-asesoria.html');

def new_asesoria(request):
    return render(request, 'cliente/asesoria/new-asesoria.html');

def detail_asesoria(request, pk):
    asesoria = Asesoria.objects.get(pk=pk)
    context = {'asesoria':asesoria}

    return render(request, 'cliente/asesoria/detail-asesoria.html', context);

def update_asesoria(request, pk):
    asesoria = Asesoria.objects.get(pk=pk)
    context = {'asesoria':asesoria}

    return render(request, 'cliente/asesoria/update-asesoria.html', context);

def list_accidente(request):

    # accidentes = Accidente.objects.all()

    # filter_tipo_accidente = request.GET.get("tipo_accidente", None)
    # if filter_tipo_accidente:
    #     # accidentes = [x for x in accidentes if filter_tipo_accidente.lower() in x.get("tipo_accidente", "").lower()]
    #     accidentes = accidentes.filter(tipo_accidente__descripcion__icontains=filter_tipo_accidente)

    # context = {"accidentes": accidentes}

    # print(context)
    # return render(request, 'cliente/accidente/list-accidente.html', context);
    return render(request, 'cliente/accidente/list-accidente.html');

def new_accidente(request):
    return render(request, 'cliente/accidente/new-accidente.html');

def detail_accidente(request, pk):
    accidente = Accidente.objects.get(pk=pk)
    context = {'accidente':accidente}

    return render(request, 'cliente/accidente/detail-accidente.html', context);

def update_accidente(request, pk):
    accidente = Accidente.objects.get(pk=pk)
    context = {'accidente':accidente}

    return render(request, 'cliente/accidente/update-accidente.html', context);

def list_capacitacion(request):
    return render(request, 'cliente/capacitacion/list-capacitacion.html');

def detail_capacitacion(request, pk):
    capacitacion = Capacitacion.objects.get(pk=pk)
    context = {'capacitacion':capacitacion}

    return render(request, 'cliente/capacitacion/detail-capacitacion.html', context);

def list_contrato(request):
    return render(request, 'cliente/contrato/list-contrato.html');

def detail_contrato(request, pk):
    contrato = Contrato.objects.get(pk=pk)
    context = {'contrato':contrato}

    return render(request, 'cliente/contrato/detail-contrato.html', context)

def list_visita(request):
    return render(request, 'cliente/visita/list-visita.html');

def detail_visita(request, pk):
    visita = Visita.objects.get(pk=pk)
    context = {'visita':visita}

    return render(request, 'cliente/visita/detail-visita.html', context);

def list_factura(request):
    return render(request, 'cliente/factura/list-factura.html');

def detail_factura(request, pk):
    factura = Factura.objects.get(pk=pk)
    context = {'factura':factura}

    return render(request, 'cliente/factura/detail-factura.html', context);

def list_item(request):
    return render(request, 'cliente/formulario-visita/list-item.html');