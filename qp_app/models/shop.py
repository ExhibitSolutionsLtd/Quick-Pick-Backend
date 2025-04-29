from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ref_number = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    date_added = models.DateField(auto_now_add=True)
    manager = models.CharField(max_length=100)

    def __str__(self):
        return f'Shop: {self.name}'
    