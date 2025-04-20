from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    CHOICES_USER_TYPE = [
        ('oddiy', 'Oddiy'),
        ('dile', 'Diler')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=5, choices=CHOICES_USER_TYPE, default=CHOICES_USER_TYPE[0][0])
    phone = models.CharField(max_length=13)
    avatar = models.ImageField(upload_to='users_avatars/')
    location = models.CharField(max_length=255)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username