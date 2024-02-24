from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator


# Create your models here.
class BlogUser(AbstractUser):
    # Add any additional fields you need here
    middle_name = models.CharField(max_length=10, blank=True, null=True)
    contact_no = models.CharField(max_length=10,blank=True,null=True)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username