from django.db import models

class Debt(models.Model):
    customer=models.CharField(max_length=200)
    customer_birth_date=models.DateField(blank=True, null=True)
    date=models.DateField(auto_now_add=True)
    products=models.CharField(max_length=500)
    debt=models.FloatField()

    def __str__(self):
        return f"{self.customer}  - {self.debt} So'm"
