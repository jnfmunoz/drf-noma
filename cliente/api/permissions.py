from rest_framework import permissions

class OwnerDetail(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # solo el creador del objeto puede ver el detalle 
        return obj.fkCliente == request.user