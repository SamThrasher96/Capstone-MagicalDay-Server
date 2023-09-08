from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)