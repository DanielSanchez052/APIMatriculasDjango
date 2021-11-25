import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from api.user.models.User import User
from api.course.serializers.general_serializers import StudentCourseSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['identification_number', 'email', 'name', 'last_name', 'city', 'direction', 'phone_number',
                  'date_born', 'gender', 'person_type', 'password']

    def validate_password(self, data):
        validators.validate_password(password=data, user=User)
        return data

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','identification_number', 'email', 'name', 'last_name', 'city', 'direction', 'phone_number', 'date_born', 'gender', 'person_type']

        def to_representation(self, instance):
            return {
                'id': instance.id,
                'identification_number': instance.identification_number,
                'email': instance.email,
                'name': instance.name,
                'last_name': instance.last_name,
                'city': instance.city,
                'phone_number': instance.phone_number,
                'direction': instance.direction,
                'date_born': instance.date_born,
                'gender': instance.gender,
                'person_type': instance.person_type}


class UserCourseListSerializer(serializers.ModelSerializer):
    courses = StudentCourseSerializer(many=True)

    class Meta:
        model = User
        fields = ['identification_number', 'email', 'name', 'last_name', 'city', 'direction', 'phone_number', 'date_born', 'gender', 'person_type', 'courses']

