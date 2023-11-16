from rest_framework.views import APIView
from rest_framework.response import Response
from paypalrestsdk import Payment
from asesora.models import Factura

class ProcesarPagoView(APIView):
    def post(self, request, *args, **kwargs):
        factura_id= request.data.get('factura_id')
        factura = Factura.objects.get(id=factura)

        #Crear pago paypal
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method":"paypal"
            },
            "transactions": {
                "amount": {
                    "total": str(factura.total_factura),
                    "currency": "USD",
                },
            },
            "description": f"Pago de factura{factura_id}",
        })
                                      