from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views
from school.views import SchoolView, RegisterView, StudentView, TeacherView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='School Backend', permission_classes=[AllowAny])),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


router = routers.SimpleRouter()
router.register(r'api/register', RegisterView)
router.register(r'api/school', SchoolView)
router.register(r'api/student', StudentView)
router.register(r'api/teacher', TeacherView)
urlpatterns += router.urls