from django.db import models
from .category import Category
from .company import Company

class Product(models.Model):
    barcode = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} ({self.barcode})"
