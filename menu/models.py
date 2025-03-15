from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Coffe-Based Drinks'),
        ('non_coffee', 'Non-Coffee Drinks'),
        ('cold', 'Cold & Blended Drinks'),
        ('food', 'Food & Pastries'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu/images/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='coffee')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name