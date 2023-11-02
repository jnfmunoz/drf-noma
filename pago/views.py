from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings
# from transbank.webpay.webpay_plus import WebpayPlus
from transbank.webpay.webpay_plus.transaction import Transaction
from django.http import JsonResponse

from asesora.models import Factura

def iniciar_pago(request, factura_id):
    # Obtiene el id de la factura de la solicitud POST
    factura_id = request.POST.get('factura_id')

    # Obten la factura y su información de tu base de datos
    factura = Factura.objects.get(id=factura_id)
    total_a_pagar = factura.total_factura

    # Crear una instancia de la transacción
    transaction = Transaction()

    # Inicia la transacción con Transbank
    response = transaction.create(
        buy_order=factura_id,
        session_id=str(factura_id),
        amount=total_a_pagar,
        return_url=settings.TRANSBANK['RETURN_URL'],
    )

    url_redirect = response.get('url', '')

    return redirect(url_redirect)

def retorno_pago(request):

    token_ws = request.GET.get('token_ws')

    try:
        response = Transaction.commit(token_ws)
        
        if response.type == "REVERSED" or response.type == "NULLIFIED":
            # La transacción fue revertida o anulada, puedes manejar esto según tus necesidades
            return JsonResponse({'message': 'Transacción anulada o revertida'})
        elif response.type == "AUTHORIZED":
            # La transacción fue autorizada, puedes actualizar el estado de la factura a "pagada"
            factura_id = int(response.buy_order)
            factura = Factura.objects.get(id=factura_id)
            factura.pagada = True
            factura.save()
            return JsonResponse({'message': 'Pago procesado con éxito'})
            # return redirect(settings.TRANSBANK['WEBPAY_URL'])
        
    except Exception as e:
        # Manejar cualquier error o excepción que pueda ocurrir
        return JsonResponse({'error': str(e)})
