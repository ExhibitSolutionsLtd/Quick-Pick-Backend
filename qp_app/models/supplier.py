from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .company import Company

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="Unnamed")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='supplier')
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    total_purchases = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )

    def __str__(self):
        return self.name