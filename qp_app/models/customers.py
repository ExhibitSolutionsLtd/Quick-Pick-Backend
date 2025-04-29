from django.db import models
from .company import Company

class Customer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    total_purchases = models.IntegerField(default=0)

    def __str__(self):
        return f'Customer: {self.full_name}'
    


