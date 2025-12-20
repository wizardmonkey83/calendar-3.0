from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    # uses email to log in
    USERNAME_FIELD = "email"
    # email required by default
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
