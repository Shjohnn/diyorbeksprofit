from django.db import models

class Debt(models.Model):
    customer=models.CharField(max_length=200)
    customer_birth_date=models.CharField(blank=True, null=True, max_length=200)
    date=models.CharField(blank=True, max_length=200)
    products=models.CharField(max_length=500)
    debt=models.IntegerField()

    def __str__(self):
        return f"{self.customer}  - {self.debt} So'm"
