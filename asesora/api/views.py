from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response

from asesora.models import Region, Comuna
from .serializers import RegionSerializer, ComunaSerializer

class RegionComunaListCreateView(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.get(("regiones"), []) # Obtiene la lista de regiones del json
        
        try: 
            for region_data in data:
                region_name = region_data["region"]
                comunas = region_data.get("comunas", [])

                region = Region.objects.create(descripcion=region_name)

                for comuna_nombre in comunas:
                    Comuna.objects.create(descripcion=comuna_nombre, region=region)
            return Response("Datos insertados correctamente.", status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response("Error al insertar datos: "  + str(e), status=status.HTTP_400_BAD_REQUEST)