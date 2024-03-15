from django.db import models

class Vegetables(models.Model):
    # Define your model fields here
    product = models.CharField(max_length=100)
    date = models.DateField()
    maximum_price = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_price = models.DecimalField(max_digits=10, decimal_places=2)
    average_price = models.DecimalField(max_digits=10, decimal_places=2)
