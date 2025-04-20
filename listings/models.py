from django.db import models
from django.contrib.auth.models import User
from cars.models import Car


class Listing(models.Model):
    CURRENCY_CHOICES = [
        ('UZS', 'So‘m'),
        ('USD', 'AQSh dollari'),
    ]

    CONDITION_CHOICES = [
        ('new', 'Yangi'),
        ('used', 'Ishlatilgan'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    location = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    is_negotiable = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.title
