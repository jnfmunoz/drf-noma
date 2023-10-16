from rest_framework import serializers
from asesora.models import Asesoria

class ListAsesoriaSerializer(serializers.ModelSerializer):

    tipo_asesoria = serializers.CharField(source='tipo_asesoria.descripcion') 
    estado_asesoria = serializers.CharField(source='estado_asesoria.descripcion')
    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Asesoria
        fields = '__all__'

class CreateAsesoriaSerializer(serializers.ModelSerializer):

    fkCliente = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Asesoria
        # fields = '__all__'
        exclude = ['fecha_termino', 'estado_asesoria', 'fkProfesional']
        estado_asesoria = serializers.CharField(source='estado_asesoria.descripcion')
        tipo_asesoria = serializers.CharField(source='tipo_asesoria.descripcion')
        

    def create(self, validated_data):
        return Asesoria.objects.create(**validated_data)
    
class DetailAsesoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asesoria
        exclude = ['fkCliente']


