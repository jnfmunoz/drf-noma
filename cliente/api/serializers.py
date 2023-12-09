from rest_framework import serializers
from asesora.models import Asesoria, Accidente, Capacitacion, Contrato, Visita, Factura, FormularioVisita, DetalleFormulario
from datetime import date

class ListAsesoriaSerializer(serializers.ModelSerializer):

    tipo_asesoria = serializers.CharField(source='tipo_asesoria.descripcion') 
    estado_asesoria = serializers.CharField(source='estado_asesoria.descripcion')
    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Asesoria
        fields = '__all__'  
        ordering = ['-fecha_creacion']

class UpdateCreateAsesoriaSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Asesoria
        exclude = ['descripcion', 'fecha_creacion', 'fecha_termino', 'estado_asesoria', 'fkProfesional']
        estado_asesoria = serializers.CharField(source='estado_asesoria.descripcion')
        tipo_asesoria = serializers.CharField(source='tipo_asesoria.descripcion')
        
    def create(self, validated_data):
        return Asesoria.objects.create(**validated_data)
    
    def validate_nombre_fiscalizador(self, value):
        if len(value) <= 5:
           raise serializers.ValidationError("El nombre del fiscalizador es muy corto!")
        else:
            return value
        
    def validate_numero_fiscalizador(self, value):
        if len(value) < 12 or len(value) > 12:
            raise serializers.ValidationError("El número del fiscalizador es muy corto!")
        else:
            return value
    
class DetailAsesoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asesoria
        exclude = ['fkCliente']

class ListAccidenteSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True) 

    class Meta:
        model = Accidente
        fields = '__all__'

class UpdateCreateAccidenteSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Accidente
        fields = '__all__'
        tipo_accidente = serializers.CharField(source='tipo_accidente.descripcion')

    def create(self, validated_data):
        return Accidente.objects.create(**validated_data)
    
    def validate_cantidad_involucrados(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ingrese una cantidad válidad de involucrados en el accidente")
        else:
            return value
        
    def validate_descripcion(self, value):
        if len(value) <= 15:
            raise serializers.ValidationError("Ingrese al menos 15 caracteres en el informe de la situación")
        else:
            return value
        
    # def validate_fecha_accidente(self, value):
    #     if value > date.today():
    #         raise serializers.ValidationError("Ingrese una fecha válida")
    #     else:
    #         return value

class DetailAccidenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accidente
        exclude = ['fkCliente']

class ListCapacitacionSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)
    fkEstadoCapacitacion = serializers.CharField(source='fkEstadoCapacitacion.descripcion')
    fkProfesional = serializers.StringRelatedField(read_only=True)
    fkComuna = serializers.StringRelatedField(source='fkComuna.descripcion')

    class Meta:
        model = Capacitacion
        fields = '__all__'

class DetailCapacitacionSerializer(serializers.ModelSerializer):

    fkProfesional = serializers.StringRelatedField(read_only=True)
    fkEstadoCapacitacion = serializers.CharField(source='fkEstadoCapacitacion.descripcion')

    class Meta:
        model = Capacitacion
        exclude = ['fkCliente']

class ListContratoSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Contrato
        fields = '__all__'

class DetailContratoSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Contrato
        fields = '__all__'

class ListVisitaSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)
    fkComuna = serializers.StringRelatedField(source='fkComuna.descripcion')
    fkEstadoVisita = serializers.CharField(source='fkEstadoVisita.descripcion')

    class Meta:
        model = Visita
        fields = '__all__'

class DetailVisitaSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)
    fkComuna = serializers.StringRelatedField(source='fkComuna.descripcion')
    fkEstadoVisita = serializers.CharField(source='fkEstadoVisita.descripcion')
    fkProfesional = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Visita
        fields = '__all__'

class ListFacturaSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True) 
    fkEstadoFactura = serializers.StringRelatedField(read_only=True) 

    class Meta:
        model = Factura
        fields = '__all__'

class DetailFacturaSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True) 
    fkEstadoFactura = serializers.StringRelatedField(read_only=True) 

    class Meta:
        model = Factura
        fields = '__all__'

class DetalleFormularioSerializer(serializers.ModelSerializer):

    fkFormularioVisita = serializers.StringRelatedField(read_only=True)
    fkElementoRevision = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = DetalleFormulario
        fields = '__all__'

class FormularioVisitaSerializer(serializers.ModelSerializer):

    item = DetalleFormularioSerializer(many=True, read_only=True)
    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FormularioVisita
        fields = '__all__'