from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class  UserProfile(AbstractUser):
    gender_choices = (
        ('male','男'),
        ('female','女')
    )
