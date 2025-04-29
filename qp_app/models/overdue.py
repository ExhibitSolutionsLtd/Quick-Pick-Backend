from django.db import models
from .customers import Customer
from .product import Product
from datetime import date

class Overdue(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    installment_amount = models.DecimalField(max_digits=5, decimal_places=2)
    days_past_due = models.IntegerField(default=0)
    status = models.CharField()