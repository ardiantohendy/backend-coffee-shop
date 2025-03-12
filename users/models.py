from django.db import models
from django.contrib.auth.models import AbstractUser # digunakan agar tetap memiliki fitur bawaan Django seperti username, password

# Create your models here.

class CustomUser(AbstractUser): 
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    photo_profile = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username