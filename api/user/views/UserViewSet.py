from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from api.user.serializers.User import UserSerializer, UserListSerializer, UserCourseListSerializer


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.serializer_class.Meta.model.objects.filter(is_active=True)
        elif len(pk) == 1 and isinstance(pk, str):
            return self.serializer_class.Meta.model.objects.filter(person_type=pk.upper(),is_active=True)
        return get_object_or_404(self.serializer_class.Meta.model, identification_number=pk,
                                 is_active=True)

    @action(detail=True, methods=['GET'], url_path='user-course')
    def userCourse(self, request, pk=None):
        queryset = UserCourseListSerializer.Meta.model.objects.get(identification_number=pk, is_active=True)
        user_course = UserCourseListSerializer(queryset)
        return Response(user_course.data, status=status.HTTP_200_OK)

    def list(self, request):
        user_serialize = self.list_serializer_class(self.get_queryset(), many=True)
        return Response(user_serialize.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serialize = self.serializer_class(data=request.data)
        if user_serialize.is_valid():
            user_serialize.save()
            return Response(user_serialize.data, status=status.HTTP_200_OK)
        return Response(user_serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_queryset(pk)
        if len(pk) == 1:
            user_serializer = self.serializer_class(user,many=True)
            return Response(user_serializer.data)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_queryset(pk)
        user_serializer = self.serializer_class(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.serializer_class.Meta.model.objects.filter(identification_number=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)