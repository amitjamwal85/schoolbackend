from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from school.models import School, Student, Teacher
from school.serializers import PostSerializer, RegistrationSerializer, StudentSerializer, TeacherSerializer
from six import text_type
from rest_framework import status
from rest_framework.schemas import ManualSchema
import coreschema, coreapi
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSetPagination(PageNumberPagination):
    page_size = 10


class SchoolView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer
    queryset = School.objects.all()
    lookup_field = "pk"


class StudentView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "pk"



class TeacherView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    lookup_field = "pk"



class RegisterView(GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'

    def create(self, request):
        data = request.data
        print(f"data: {data}")
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid( raise_exception=True ):
            user = serializer.create(validated_data=serializer.validated_data)
            token = RefreshToken.for_user( user )
            data = {
                'access': text_type( token.access_token ),
                'refresh': text_type( token ),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)