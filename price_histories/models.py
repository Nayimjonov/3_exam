from django.db import models
from listings.models import Listing


class PriceHistory(models.Model):
    CURRENCY_CHOICES = [
        ('UZS', 'So‘m'),
        ('USD', 'AQSh dollari'),
    ]

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Price history for {self.listing.title}"


