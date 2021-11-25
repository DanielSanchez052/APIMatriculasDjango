from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from api.course.serializers.CourseSerializer import CourseSerializer
from api.course.serializers.general_serializers import GradesSerializer,CourseEscolarSerializer, StudentCourseSerializer, StudentCourseListSerializer


class GradesViewSet(viewsets.ModelViewSet):
    serializer_class = GradesSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(is_active=True)

    def destroy(self, request, pk=None):
        course_destroy = self.serializer_class.Meta.model.objects.filter(pk=pk).update(is_active=False)
        if course_destroy == 1:
            return Response({
                'message': 'Grado eliminado correctamente'
            })
        return Response({
            'message': 'No existe el grado que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)


class CourseEscolarViewSet(viewsets.ModelViewSet):
    serializer_class = CourseEscolarSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class StudentCourseViewSet(viewsets.ModelViewSet):
    serializer_class = StudentCourseSerializer
    list_serializer_class = StudentCourseListSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(user__is_active=True)

    def list(self, request):
        studentcourse_serialize = self.list_serializer_class(self.get_queryset(), many=True)
        return Response(studentcourse_serialize.data, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(is_active=True)

    def destroy(self, request, pk=None):
        course_destroy = self.serializer_class.Meta.model.objects.filter(pk=pk).update(is_active=False)
        if course_destroy == 1:
            return Response({
                'message': 'Curso eliminado correctamente'
            })
        return Response({
            'message': 'No existe el curso que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)