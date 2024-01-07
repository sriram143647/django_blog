from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BlogUser(AbstractUser):
    # Add any additional fields you need here

    def __str__(self):
        return self.username