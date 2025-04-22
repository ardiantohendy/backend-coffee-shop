from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Coffee-Based Drinks', 'Coffee-Based Drinks'),
        ('Non-Coffee Drinks', 'Non-Coffee Drinks'),
        ('Cold & Blended Drinks', 'Cold & Blended Drinks'),
        ('Food & Pastries', 'Food & Pastries'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu/images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Coffee-Based Drinks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name