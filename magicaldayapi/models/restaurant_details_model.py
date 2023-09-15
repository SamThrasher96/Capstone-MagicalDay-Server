from django.db import models

class RestaurantDetails(models.Model):
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    allergy_friendly = models.BooleanField()

    @property
    def restaurant_name(self):
        return self.location.name

    @property
    def restaurant_image(self):
        return self.location.image