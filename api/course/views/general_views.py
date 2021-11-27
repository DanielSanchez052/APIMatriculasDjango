from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from api.course.serializers.CourseSerializer import CourseSerializer, CourseListSerializer, StudentCourseListSerializer
from api.course.serializers.general_serializers import GradesSerializer,\
                                                            CourseEscolarSerializer, \
                                                            StudentCourseSerializer


class GradesViewSet(viewsets.ModelViewSet):
    serializer_class = GradesSerializer
    lookup_field = 'number'
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)

    def destroy(self, request, number=None):
        course_destroy = self.serializer_class.Meta.model.objects.filter(number=number).update(is_active=False)
        if course_destroy == 1:
            return Response({
                'message': 'Grado eliminado correctamente'
            })
        return Response({
            'message': 'No existe el grado que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)


class CourseEscolarViewSet(viewsets.ModelViewSet):
    serializer_class = CourseEscolarSerializer
    lookup_field = 'number'
    queryset = serializer_class.Meta.model.objects.all()


class StudentCourseViewSet(viewsets.ModelViewSet):
    serializer_class = StudentCourseSerializer
    list_serializer_class = StudentCourseListSerializer
    queryset = serializer_class.Meta.model.objects.filter(user__is_active=True)
    lookup_field = 'number'

    def list(self, request):
        studentcourse_serialize = self.list_serializer_class(self.get_queryset(), many=True)
        return Response(studentcourse_serialize.data, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    list_serializer_class = CourseListSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    lookup_field = 'number'

    def list(self, request):
        user_serialize = self.list_serializer_class(self.get_queryset(), many=True)
        return Response(user_serialize.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.list_serializer_class(instance)
        return Response(serializer.data)

    def destroy(self, request, number=None):
        course_destroy = self.serializer_class.Meta.model.objects.filter(number=number).update(is_active=False)
        if course_destroy == 1:
            return Response({
                'message': 'Curso eliminado correctamente'
            })
        return Response({
            'message': 'No existe el curso que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)