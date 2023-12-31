from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from core import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404

import requests
import datetime

from asesora.models import Asesoria, Accidente, Capacitacion, Contrato, Visita, Factura

# Create your views here.
def list_asesoria(request):

    # asesorias = Asesoria.objects.all()

    # filter_fechainicio = request.GET.get('fechainicio', False)
    # if filter_fechainicio:
    #     try:
    #         filter_fechainicio = datetime.datetime.strptime(filter_fechainicio, '%Y-m-d%').date()
    #         asesorias = asesorias.filter(fechainicio__gte=filter_fechainicio)
    #     except ValueError:
    #         pass

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
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(factura.total_factura),
        'item_name': 'Pago Servicios',
        'invoice': str(factura.pk),
        'currency': 'USD', #CLP
        'custom': str(factura.pk),
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-return")}?id_factura={factura.pk}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form, 'factura': factura}

    return render(request, 'cliente/factura/detail-factura.html', context);

def paypal_return(request):

    # Obtén la URL completa, incluyendo los parámetros
    # return_url = request.get_full_path()

    # Imprime o registra la URL en la consola o el sistema de registro
    # print(f'Return URL from PayPal: {return_url}')

    # Obtén el ID de la factura desde el parámetro en la URL o desde donde lo tengas
    factura_id = request.GET.get('id_factura')

    # Asegúrate de manejar adecuadamente el caso en el que el ID no esté presente
    if not factura_id:
        messages.error(request, 'Invalid request. Factura ID not provided.')
        return redirect('factura-list')

    # Obtén la factura correspondiente
    factura = get_object_or_404(Factura, pk=factura_id)

    # Marcar la factura como pagada
    factura.pagado = True
    factura.save()

    messages.success(request,'You\'ve successfully made a payment!')
    
    return redirect('factura-list')

def paypal_cancel(request):
    
    messages.success(request,'Your order has been cancelled.')
    return redirect('factura-list')

def list_item(request):
    return render(request, 'cliente/formulario-visita/list-item.html');