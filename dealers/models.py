from django.db import models
from django.contrib.auth.models import User


class Dealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dealer')
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    website = models.URLField()
    address = models.TextField()
    is_verified = models.BooleanField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        reviews = self.reviews.all()
        if reviews:
            self.rating = sum(review.rating for review in reviews) / reviews.count()
        else:
            self.rating = 0.0
        self.save()
