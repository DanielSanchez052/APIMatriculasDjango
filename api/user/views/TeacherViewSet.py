from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from api.user.serializers.serializers import TeacherSerializer, TeacherListSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    list_serializer_class = TeacherListSerializer
    queryset = serializer_class.Meta.model.objects.all()
    lookup_field = 'number'

    def list(self, request):
        user_serialize = self.list_serializer_class(self.get_queryset(), many=True)
        return Response(user_serialize.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.list_serializer_class(instance)
        return Response(serializer.data)