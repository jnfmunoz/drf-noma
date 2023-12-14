from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received

from .models import Factura

@receiver(valid_ipn_received)
def valid_ipn_received(sender, **kwargs):
    print("Valid ipn received")
    ipn = sender
    if ipn.payment_status == 'Completed':
        factura_id = ipn.custom
        try: 
            factura = Factura.objects.get(pk=factura_id)
            factura.pagado = True
            factura.save()

        except Factura.DoesNotExist:
            print(f"Factura con ID {factura_id} no encontrado")
            
@receiver(invalid_ipn_received)
def invalid_ipn_received(sender, **kwargs):
    print("Invalid IPN received")
    ipn = sender
    if ipn.payment_status == 'Completed':
        # Obtener el ID de la factura desde 'custom'
        factura_id = ipn.custom
        try:
            # Obtener la factura correspondiente y marcarla como pagada
            factura = Factura.objects.get(pk=factura_id)
            factura.pagado = True
            factura.save()
        except Factura.DoesNotExist:
            print(f"Factura con ID {factura_id} no encontrada. No se marcará como pagada.")
