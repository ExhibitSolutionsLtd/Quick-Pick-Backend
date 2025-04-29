from django.db import models
from .customers import Customer

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, related_name='purchases', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer.phone_number} - {self.amount} on {self.purchase_date}"
