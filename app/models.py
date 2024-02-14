from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Course(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title