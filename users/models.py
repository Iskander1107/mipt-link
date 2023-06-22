from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)