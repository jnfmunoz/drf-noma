from rest_framework import serializers
from asesora.models import Asesoria, Accidente, Capacitacion, Contrato

class ListAsesoriaSerializer(serializers.ModelSerializer):

    tipo_asesoria = serializers.CharField(source='tipo_asesoria.descripcion') 
    estado_asesoria = serializers.CharField(source='estado_asesoria.descripcion')
    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Asesoria
        fields = '__all__'

class UpdateCreateAsesoriaSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Asesoria
        exclude = ['descripcion', 'fecha_creacion', 'fecha_termino', 'estado_asesoria', 'fkProfesional']
        estado_asesoria = serializers.CharField(source='estado_asesoria.descripcion')
        tipo_asesoria = serializers.CharField(source='tipo_asesoria.descripcion')
        
    def create(self, validated_data):
        return Asesoria.objects.create(**validated_data)
    
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