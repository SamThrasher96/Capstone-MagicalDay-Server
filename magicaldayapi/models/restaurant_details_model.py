from django.db import models

class RestaurantDetails(models.Model):
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    allergy_friendly = models.BooleanField()