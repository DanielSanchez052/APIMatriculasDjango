from rest_framework import serializers

from api.course.models.Grades import Grades
from api.course.models.CourseEscolar import CourseEscolar
from api.course.models.StudentCourse import StudentCourse
from api.course.serializers.CourseSerializer import CourseSerializer


class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ['id', 'name']


class CourseEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEscolar
        fields = ['id', 'start_year', 'end_year']


class StudentCourseListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    course = CourseSerializer(read_only=True)
    course_escolar = serializers.StringRelatedField()

    def validate_user(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError("This field may not be blank.")
        return value

    def validators(self, data):
        if 'user' not in data.keys():
            raise serializers.ValidationError({
                "user": "This field may not be blank."
            })
        return data

    class Meta:
        model = StudentCourse
        fields = '__all__'


class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'
