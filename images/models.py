from django.db import models
from listings.models import Listing


class Image(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='car_images/')
    is_primary = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Image for {self.listing.title} (Primary: {self.is_primary})"
