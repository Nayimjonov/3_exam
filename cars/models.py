from django.db import models
from vehicles.models import Make, Model, BodyType, Feature


class Car(models.Model):
    FUEL_CHOICES = [
        ('gasoline', 'Benzin'),
        ('diesel', 'Dizel'),
        ('electric', 'Elektr'),
        ('hybrid', 'Gibrid'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Mexanik'),
        ('automatic', 'Avtomatik'),
        ('cvt', 'CVT'),
        ('semi-automatic', 'Yarim avtomatik'),
    ]

    DRIVE_TYPE_CHOICES = [
        ('fwd', 'Old balon'),
        ('rwd', 'Orqa balon'),
        ('awd', 'Toliq yuruvchi'),
    ]

    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=30)
    mileage = models.PositiveIntegerField()
    engine_size = models.FloatField()
    power = models.PositiveIntegerField()
    drive_type = models.CharField(max_length=20, choices=DRIVE_TYPE_CHOICES)
    features = models.ManyToManyField(Feature, blank=True)
    vin = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make.name} {self.model.name}"