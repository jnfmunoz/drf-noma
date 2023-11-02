from rest_framework.response import Response
from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend 

from asesora.models import Asesoria, Accidente, Capacitacion, Contrato, Visita, Factura, FormularioVisita, DetalleFormulario
from .serializers import (ListAsesoriaSerializer, UpdateCreateAsesoriaSerializer, DetailAsesoriaSerializer, 
                          ListAccidenteSerializer,UpdateCreateAccidenteSerializer, DetailAccidenteSerializer,
                          ListCapacitacionSerializer, DetailCapacitacionSerializer, ListContratoSerializer,
                          DetailContratoSerializer, ListVisitaSerializer, DetailVisitaSerializer, ListFacturaSerializer,
                          DetailFacturaSerializer, FormularioVisitaSerializer, DetalleFormularioSerializer)
from .permissions import OwnerDetail
from .filters import AccidenteFilter

class AsesoriaListAV(mixins.ListModelMixin, generics.GenericAPIView):

    permission_classes = [OwnerDetail]
    serializer_class = ListAsesoriaSerializer

    """
    Concrete view for listing a queryset.
    """
    def get_queryset(self):
        return Asesoria.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class AsesoriaCreateAV(mixins.CreateModelMixin, generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = UpdateCreateAsesoriaSerializer

    """
    Concrete view for creating a model instance.
    """
    def perform_create(self, serializer):
        cliente = self.request.user
        # Asigna el usuario autenticado como autor del objeto
        serializer.save(fkCliente=cliente)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
       
class AsesoriaDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):

    permission_classes = [OwnerDetail]
    serializer_class = DetailAsesoriaSerializer
    queryset = Asesoria.objects.all()

    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class AsesoriaUpdateAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    permission_classes = [OwnerDetail]
    serializer_class = UpdateCreateAsesoriaSerializer
    queryset = Asesoria.objects.all()

    """
    Concrete view for updating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class AccidenteListAV(mixins.ListModelMixin, generics.GenericAPIView):
    
    permission_classes = [OwnerDetail]
    serializer_class = ListAccidenteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AccidenteFilter # Filtro personalizado

    """
    Concrete view for listing a queryset.
    """
    def get_queryset(self):
        return Accidente.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class AccidenteCreateAV(mixins.CreateModelMixin, generics.GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateCreateAccidenteSerializer

    """
    Concrete view for creating a model instance.
    """
    def perform_create(self, serializer):
        cliente = self.request.user
        # Asigna el usuario autenticado como autor del objeto
        serializer.save(fkCliente=cliente)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class AccidenteDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):
    
    permission_classes = [OwnerDetail]
    serializer_class = DetailAccidenteSerializer
    queryset = Accidente.objects.all()

    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class AccidenteUpdateAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin , generics.GenericAPIView):
    
    permission_classes = [OwnerDetail]
    serializer_class = UpdateCreateAccidenteSerializer
    queryset = Accidente.objects.all()
    
    """
    Concrete view for updating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class CapacitacionListAV(mixins.ListModelMixin, generics.GenericAPIView):

    # permission_classes = [OwnerDetail]
    serializer_class = ListCapacitacionSerializer

    """
    Concrete view for listing a queryset.
    """
    def get_queryset(self):
        return Capacitacion.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CapacitacionDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):


    serializer_class = DetailCapacitacionSerializer
    queryset = Capacitacion.objects.all()

    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class ContratoListAV(mixins.ListModelMixin, generics.GenericAPIView):

    # permission_classes = [OwnerDetail]
    serializer_class = ListContratoSerializer

    """
    Concrete view for listing a queryset.
    """
    def get_queryset(self):
        return Contrato.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ContratoDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):


    serializer_class = DetailContratoSerializer
    queryset = Contrato.objects.all()

    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class VisitaListAV(mixins.ListModelMixin, generics.GenericAPIView):

    # permission_classes = []
    serializer_class = ListVisitaSerializer

    """
    Concrete view for listing a queryset.
    """
    def get_queryset(self):
        return Visita.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class VisitaDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):

    serializer_class = DetailVisitaSerializer
    queryset = Visita.objects.all()

    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class FacturaListAV(mixins.ListModelMixin, generics.GenericAPIView):

    # permission_classes = []
    serializer_class = ListFacturaSerializer

    """
    Concrete view for listing a queryset.
    """
    def get_queryset(self):
        return Factura.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class FacturaDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):

    serializer_class = DetailFacturaSerializer
    queryset = Factura.objects.all()

    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class FormularioVisitaAV(mixins.ListModelMixin, generics.GenericAPIView):

    serializer_class = FormularioVisitaSerializer
    
    def get_queryset(self):
        return FormularioVisita.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class DetalleFormularioAV(mixins.ListModelMixin, generics.GenericAPIView):

    serializer_class = DetalleFormularioSerializer
    queryset = DetalleFormulario.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)