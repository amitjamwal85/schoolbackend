from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from school.models import School, USER_TYPES, Student, Teacher
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['school_name', 'school_address', 'school_phone']

def required_and_valid(value):
    if value is None:
        raise serializers.ValidationError('This field is required')
    return True


def required_field():
    return serializers.CharField(required=True)


def password_field():
    return serializers.CharField(
        max_length=32,
        min_length=8,
        required=True
    )


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[required_and_valid, UniqueValidator(queryset=User.objects.all())])
    password = password_field()
    first_name = required_field()
    last_name = required_field()
    user_type = serializers.ChoiceField(required=True, choices=USER_TYPES)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'user_type']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[required_and_valid, UniqueValidator(queryset=User.objects.all())])
    first_name = required_field()
    last_name = required_field()

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'skill_level', 'instrument', 'student_since', 'birthday', 'teacher', 'school', 'user']


class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[required_and_valid, UniqueValidator(queryset=User.objects.all())])
    first_name = required_field()
    last_name = required_field()

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'teaching_since', 'instrument', 'teacher_type', 'email', 'user', 'school']