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

    @property
    def restaurant_description(self):
        return self.location.description

    @property
    def restaurant_open(self):
        return self.location.opening_time 

    @property
    def restaurant_close(self):
        return self.location.closing_time