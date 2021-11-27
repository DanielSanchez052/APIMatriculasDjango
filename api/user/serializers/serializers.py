from rest_framework import serializers

from api.user.models.Department import Department
from api.user.models.Teacher import Teacher
from api.user.models.User import User
from api.user.serializers.User import UserSerializer


class UserMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['identification_number', 'name', 'last_name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'number', 'name']


class TeacherListSerializer(serializers.ModelSerializer):
    person = UserSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Teacher
        fields = ['number', 'person', 'department']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['number', 'person', 'department']
