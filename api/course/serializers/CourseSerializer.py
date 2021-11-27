from rest_framework import serializers

from api.course.models.Course import Course
from api.user.serializers.serializers import TeacherListSerializer
from api.course.serializers.general_serializers import GradesSerializer
from api.course.models.StudentCourse import StudentCourse


class CourseListSerializer(serializers.ModelSerializer):
    teacher = TeacherListSerializer()
    grade = GradesSerializer()

    class Meta:
        model = Course
        exclude = ('is_active', 'created_at', 'modified_at', 'deleted_at')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('is_active', 'created_at', 'modified_at', 'deleted_at')


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