from asesora.models import Asesoria
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ListAsesoriaSerializer, CreateAsesoriaSerializer, DetailAsesoriaSerializer
from .permissions import OwnerDetail

class AsesoriaListAV(mixins.ListModelMixin, generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ListAsesoriaSerializer

    def get_queryset(self):
        return Asesoria.objects.filter(fkCliente_id=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class AsesoriaCreateAV(mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = CreateAsesoriaSerializer

    def perform_create(self, serializer):
        cliente = self.request.user
        # Asigna el usuario autenticado como autor del objeto
        serializer.save(fkCliente=cliente)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class AsesoriaDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = Asesoria.objects.all()
    serializer_class = DetailAsesoriaSerializer
    permission_classes = [OwnerDetail]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

