from django.db import models


# Create your models here.
class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
