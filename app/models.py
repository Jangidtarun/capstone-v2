from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    
class Semester(models.Model):
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title


class Course(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=64)
    course_code = models.CharField(max_length=8)
    grade = models.PositiveIntegerField()
    credit = models.PositiveIntegerField()
    elective_type_choices = {

    }
    elective_type = models.CharField(max_length=64, choices=elective_type_choices)

    def __str__(self) -> str:
        return f'{self.title}'