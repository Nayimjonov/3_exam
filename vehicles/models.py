from django.db import models
from django.contrib.auth.models import User

class Make(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class BodyType(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='body_types/')

class Feature(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class Listing(models.Model):
    title = models.CharField(max_length=200)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True, blank=True)
    features = models.ManyToManyField(Feature, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SavedListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class ComparisonList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(Listing)
