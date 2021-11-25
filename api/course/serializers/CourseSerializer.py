from rest_framework import serializers
from api.course.models.Course import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('is_active', 'created_at', 'modified_at', 'deleted_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            "name": instance.name,
            "credit": instance.credit,
            "type": instance.type,
            "course": instance.course,
            "quarter": instance.quarter,
            "teacher": instance.teacher.__str__(),
            "grade": instance.grade.__str__()
        }
