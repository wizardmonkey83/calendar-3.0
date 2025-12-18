from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    # keep forgetting how to set non-required fields. but i think this does it.
    home_address = models.CharField(blank=True)