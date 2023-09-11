from django.db import models

class RestaurantDetails(models.Model):
    description = models.CharField(max_length=500)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    