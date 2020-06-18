from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from schoolbackend import settings
from django.db.models.signals import post_save


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    school_name = models.CharField(max_length=100, null=True)
    school_address = models.CharField(max_length=100, null=True)
    school_phone = models.CharField(max_length=100, null=True)


STUDENT = "student"
TEACHER = "teacher"

USER_TYPES = (
    (STUDENT, "student"),
    (TEACHER, "teacher"),
)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    user_type = models.CharField(choices=USER_TYPES,
                                 max_length=10,
                                 null=False)

Administrator = "administrator"
Assistant = "assistant"
Regularteacher = "regularteacher"

TEACHER_TYPES = (
    (Administrator, "administrator"),
    (Assistant, "assistant"),
    (Regularteacher,"regularteacher")
)


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    teaching_since = models.DateField(null=True)
    instrument = models.CharField(max_length=100, null=True)
    teacher_type = models.CharField(choices=TEACHER_TYPES,
                                  max_length=20,
                                  default="administrator")
    email = models.CharField(max_length=100, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_teacher"
    )
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, related_name="school_teacher", null=True)



class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    skill_level = models.CharField(max_length=100, null=True)
    instrument = models.CharField(max_length=100, null=True)
    student_since = models.DateField(null=True)
    email = models.CharField(max_length=100, null=True)
    birthday = models.CharField(max_length=100, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name="teacher", null=True)
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, related_name="school_student", null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_student"
    )



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def setup_user(sender, instance, created, **kwargs):
    if created:
        if instance.first_name == 'student':
            Student.objects.create(user=instance,
                                   first_name=instance.first_name,
                                   last_name=instance.last_name,
                                   email= instance.email)
        else:
            Teacher.objects.create(user=instance,
                                   first_name=instance.first_name,
                                   last_name=instance.last_name,
                                   email=instance.email)

            