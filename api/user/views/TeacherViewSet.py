from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


from api.user.serializers.serializers import TeacherSerializer, TeacherListSerializer
from api.user.serializers.User import UserSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    list_serializer_class = TeacherListSerializer

    def get_queryset(self, pk=None):
        return self.serializer_class.Meta.model.objects.all()

    def list(self, request):
        user_serialize = self.list_serializer_class(self.get_queryset(), many=True)
        return Response(user_serialize.data, status=status.HTTP_200_OK)
