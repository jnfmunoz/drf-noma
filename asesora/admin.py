from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Asesoria)
admin.site.register(models.EstadoAsesoria)
admin.site.register(models.TipoAsesoria)
admin.site.register(models.TipoAccidente)
admin.site.register(models.Cliente)
admin.site.register(models.Accidente)
admin.site.register(models.Profesional)
admin.site.register(models.Capacitacion)