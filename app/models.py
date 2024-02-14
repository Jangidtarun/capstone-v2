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
    title = models.CharField(max_length=64)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='sem')

    def __str__(self) -> str:
        return f'{self.title} in {self.semester.pk}'