from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length = 200)
    user_type = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.username