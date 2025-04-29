from django.db import models
from django.contrib.auth.models import User
from datetime import date

from .supplier import Supplier
from .payment_type import PaymentType
from .category import Category

class ExpenseModel(models.Model):
    date = models.DateField(default=date.today)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2, default='0.00')  
    payment_type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, default="No description")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supplier} - {self.date}"
