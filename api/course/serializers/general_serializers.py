from rest_framework import serializers

from api.course.models.Grades import Grades
from api.course.models.CourseEscolar import CourseEscolar
from api.course.models.StudentCourse import StudentCourse


class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ['id', 'number', 'name']


class CourseEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEscolar
        fields = ['id', 'number', 'start_year', 'end_year']


class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'
