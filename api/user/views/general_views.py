from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from api.user.serializers.serializers import DepartmentSerializer



class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(is_active=True)

    def destroy(self, request, pk=None):
        course_destroy = self.serializer_class.Meta.model.objects.filter(pk=pk).update(is_active=False)
        if course_destroy == 1:
            return Response({
                'message': 'Departamento eliminado correctamente'
            })
        return Response({
            'message': 'No existe el departamento que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)


