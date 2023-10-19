from rest_framework import serializers
from asesora.models import Asesoria, Accidente

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
        # fields = '__all__'
        exclude = ['fecha_creacion','fecha_termino', 'estado_asesoria', 'fkProfesional']
        estado_asesoria = serializers.CharField(source='estado_asesoria.descripcion')
        tipo_asesoria = serializers.CharField(source='tipo_asesoria.descripcion')
        
    def create(self, validated_data):
        return Asesoria.objects.create(**validated_data)
    
class DetailAsesoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asesoria
        exclude = ['fkCliente']

class ListAccidenteSerializer(serializers.ModelSerializer):

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