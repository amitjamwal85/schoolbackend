from django.contrib import admin

from school.models import School, User


@admin.register(School)
class AddS3FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_name', 'school_address', 'school_phone')


@admin.register(User)
class AddS3FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_superuser', 'email', 'is_staff', 'is_active')
