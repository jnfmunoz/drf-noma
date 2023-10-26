from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Region(models.Model):

    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.descripcion
    
class Comuna(models.Model):

    descripcion = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.descripcion

class TipoAsesoria(models.Model):

    # Accidente, Fiscalización
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.descripcion

class TipoAccidente(models.Model):

    # Por caída, Por exposición o contacto, Por sobreesfuerzo o golpes, Por movimientos repetitivos
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.descripcion
    
class TipoEmpresa(models.Model):

    # Industrial, Minero, Construcción
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.descripcion

class TipoPago(models.Model):

    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.descripcion

class EstadoAsesoria(models.Model):
    
    # Agendada, En Curso, Finalizada, Cancelada
    descripcion = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.descripcion

class EstadoFactura(models.Model):

    descripcion = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.descripcion

class EstadoVisita(models.Model):

    descripcion = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.descripcion

class EstadoCapacitacion(models.Model):

    descripcion = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.descripcion

class EstadoServicio(models.Model):

    descripcion = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.descripcion

class Usuario(models.Model):
    
    # user_auth = models.OneToOneField(User, on_delete=models.PROTECT)
    password = models.CharField(max_length=128)
    # last_login = models.DateTimeField(null=True, blank=True) #Por defecto que sea null
    # is_superurser = models.BooleanField() #Por defecto que sea 0
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    # is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateField(auto_now_add=True)    
    # tipo_usuario = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    auth_group = models.ForeignKey(Group, on_delete=models.PROTECT)

class Administrador(models.Model):
    
    fkUser = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Administrador", related_name="admin_user")
    rut = models.CharField(max_length=8)
    dv = models.CharField(max_length=1)
    fecha_inicio_contrato = models.DateField()    
    fecha_fin_contrato = models.DateField()
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    nro_telefono = models.CharField(max_length=20)
    disponibilidad = models.BooleanField()
    fkComuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, verbose_name='Comuna')

    def __str__(self) -> str:
        return self.rut + "-" + self.dv
    

class Cliente(models.Model):

    rut = models.CharField(max_length=8)
    dv = models.CharField(max_length=1)
    razon_legal = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fkComuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, verbose_name='Comuna')
    fkEstadoServicio = models.ForeignKey(EstadoServicio, on_delete=models.PROTECT, verbose_name="EstadoServicio")
    fkTipoEmpresa = models.ForeignKey(TipoEmpresa, on_delete=models.PROTECT, verbose_name='TipoEmpresa', related_name='tipo_empresa')
    fkUser = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario', related_name='client_user')
    
    def __str__(self) -> str:
        return self.rut + "-" + self.dv

class Profesional(models.Model):

    fkUser = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Usuario', related_name='profesional_user')
    rut = models.CharField(max_length=8)
    dv = models.CharField(max_length=1)
    fecha_inicio_contrato = models.DateField()    
    fecha_fin_contrato = models.DateField()
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    nro_telefono = models.CharField(max_length=20)
    disponibilidad = models.BooleanField()
    fkComuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, verbose_name='Comuna')

    def __str__(self) -> str:
        return self.rut + "-" + self.dv

class Asesoria(models.Model):

    fkCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente')
    fkProfesional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profesional_asignado', default=None, null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_termino = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    nombre_fiscalizador = models.CharField(max_length=200)
    numero_fiscalizador = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tipo_asesoria = models.ForeignKey(TipoAsesoria, on_delete=models.PROTECT, related_name="tipo_asesoria")
    estado_asesoria = models.ForeignKey(EstadoAsesoria, on_delete=models.PROTECT, related_name="estado_asesoria", default=1)

    def __str__(self) -> str:
        return str(self.id)+ ' | ' + str(self.tipo_asesoria) + ' | ' + self.descripcion + ' | ' + str(self.estado_asesoria)
    
class Accidente(models.Model):

    fkCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente')
    fecha_accidente = models.DateField()
    cantidad_involucrados = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    tipo_accidente = models.ForeignKey(TipoAccidente, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.descripcion
    
class Capacitacion(models.Model):

    fkCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='cliente')
    fkProfesional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profesional', default=None, null=True, blank=True)
    descripcion = models.CharField(max_length=200)
    cant_asistente = models.IntegerField()
    # cant_asistente_final = models.IntegerField()
    lista_asist = models.JSONField(null=True)
    fecha_capacitacion = models.DateField()
    direccion = models.CharField(max_length=200)
    fkComuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, verbose_name='Comuna')
    fkEstadoCapacitacion = models.ForeignKey(EstadoCapacitacion, on_delete=models.PROTECT)
    
class Contrato(models.Model):

    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_termino = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=200)
    costo_mensual = models.IntegerField()
    costo_modificacion_formulario = models.IntegerField()
    costo_capacitacion_extra = models.IntegerField()
    costo_asesoria_extra = models.IntegerField()
    costo_llamada_extra = models.IntegerField()
    costo_actualizar_informe = models.IntegerField()
    fkCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='cliente')

class Factura(models.Model):

    fecha_emision = models.DateField(auto_now_add=True)
    fecha_vencimento = models.DateField()
    total_factura = models.DateField()
    fkEstadoFactura = models.ForeignKey(EstadoFactura, on_delete=models.PROTECT)
    fkCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='cliente')

class DetallePago(models.Model):

    fecha_pago = models.DateField(auto_now_add=True)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.PROTECT)
    fkFactura = models.ForeignKey(Factura, on_delete=models.PROTECT)

class ElementoRevision(models.Model):

    descripcion = models.CharField(max_length=200)

class FormularioVisita(models.Model):

    cant_parametro = models.IntegerField(default=0)
    con_problema = models.CharField(max_length=1)
    fkCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='cliente')

class Visita(models.Model):

    fkCliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='cliente_vista', default=None, null=True, blank=True)
    fkProfesional = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profesional_visita', default=None, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    fkComuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, verbose_name='Comuna')
    fkFormularioVisita = models.ForeignKey(FormularioVisita, on_delete=models.PROTECT)
    fkEstadoVisita = models.ForeignKey(EstadoVisita, on_delete=models.PROTECT)
    
class PlanMejora(models.Model):

    descripcion = models.CharField(max_length=200)
    fkVisita = models.OneToOneField(Visita, on_delete=models.CASCADE)

class DetalleFormulario(models.Model):

    se_cumple = models.CharField(max_length=1)
    fkFormularioVisita = models.ForeignKey(FormularioVisita, on_delete=models.PROTECT)
    fkElementoRevision = models.ForeignKey(ElementoRevision, on_delete=models.PROTECT)

class ReporteMensual(models.Model):

    fecha_reporte = models.DateField(auto_now_add=True)
    informe = models.FileField(upload_to='reportes')

class RegistroError(models.Model):

    correlativo = models.AutoField(primary_key=True, default=1)
    codigoError = models.CharField(max_length=100, default=1)
    mensajeError = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"Registro Erro {self.correlativo}"

class IdxUsr(models.Model):
    
    fkUsuario = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    fkUser = models.OneToOneField(User, on_delete=models.PROTECT)

