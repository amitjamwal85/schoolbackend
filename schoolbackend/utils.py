from rest_framework import permissions
from school.models import Teacher


all_permission_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
read_permission_methods = ['GET']




class SchoolPermission(permissions.BasePermission):
    message = {"status" : "you don't have permission"}
    def __init__(self):
        super().__init__()

    def has_permission(self, request, view):
        print(f"user_type : {request.user.user_type}")
        if request.user.user_type == 'student':
            return False
        else:
            view_class = view.__class__.__name__
            teacher = Teacher.objects.get(user=request.user)
            print(f"teacher_type: {teacher.teacher_type} # {view_class}")

            if view_class in ['SchoolView', 'StudentView', 'TeacherView']:
                if teacher.teacher_type == 'administrator' and request.method in all_permission_methods:
                    return True
                if teacher.teacher_type == 'assistant' and request.method in read_permission_methods:
                    return True
            if view_class in ['StudentView']:
                if teacher.teacher_type == 'regularteacher' and request.method in all_permission_methods:
                    return True
        return False



class MyPermission(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        print(f"request.method: {request.method} in  {self.allowed_methods}")
        return request.method in self.allowed_methods

