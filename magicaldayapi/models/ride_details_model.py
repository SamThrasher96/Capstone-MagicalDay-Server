from django.db import models

class RideDetails(models.Model):
    operating = models.BooleanField()
    height_requirement = models.JSONField() 
    duration = models.IntegerField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    expected_wait_time = models.IntegerField()

    @property
    def ride_name(self):
        return self.location.name

    @property
    def ride_image(self):
        return self.location.image

    @property
    def ride_description(self):
        return self.location.description

    @property
    def ride_open(self):
        return self.location.opening_time 

    @property
    def ride_close(self):
        return self.location.closing_time