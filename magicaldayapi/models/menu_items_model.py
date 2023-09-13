from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    image = models.CharField(max_length=500)