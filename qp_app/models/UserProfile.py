from django.db import models
from django.contrib.auth.models import User
from .roles import Role

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField( blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

