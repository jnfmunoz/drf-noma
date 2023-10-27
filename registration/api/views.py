from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from .serializers import UserSerializer

class CreateUserView(CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        first_name = serializer.validated_data['first_name']
        last_name = serializer.validated_data['last_name']
        email = serializer.validated_data['email']
        group_name = serializer.validated_data['groups_name'] 

        usuario = User(username=username, first_name=first_name, last_name=last_name, email=email)
        usuario.set_password(password)
        usuario.save()

        # group = Group.objects.get(pk=group_id)
        # usuario.groups.add(group)
        # Busca el grupo por nombre y asigna el usuario al grupo
        try:
            group = Group.objects.get(name=group_name)
            usuario.groups.add(group)
        except Group.DoesNotExist:
            # Maneja el caso en el que el grupo no se encuentra
            usuario.delete()  # Elimina el usuario si el grupo no existe
            return Response("Grupo no encontrado", status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)