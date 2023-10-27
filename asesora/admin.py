from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Accidente)
admin.site.register(models.Administrador)
admin.site.register(models.Asesoria)
admin.site.register(models.Capacitacion)
admin.site.register(models.Cliente)
admin.site.register(models.Comuna)
admin.site.register(models.Contrato)
admin.site.register(models.DetalleFormulario)
admin.site.register(models.DetallePago)
admin.site.register(models.ElementoRevision)
admin.site.register(models.EstadoAsesoria)
admin.site.register(models.EstadoCapacitacion)
admin.site.register(models.EstadoFactura)
admin.site.register(models.EstadoServicio)
admin.site.register(models.EstadoVisita)
admin.site.register(models.Factura)
admin.site.register(models.FormularioVisita)
admin.site.register(models.PlanMejora)
admin.site.register(models.Profesional)
admin.site.register(models.Region)
admin.site.register(models.RegistroError)
admin.site.register(models.ReporteMensual)
admin.site.register(models.TipoAccidente)
admin.site.register(models.TipoAsesoria)
admin.site.register(models.TipoEmpresa)
admin.site.register(models.TipoPago)
admin.site.register(models.Visita)