from django.db import models

class RideDetails(models.Model):
    operating = models.BooleanField()
    height_requirement = models.JSONField() 
    duration = models.IntegerField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    expected_wait_time = models.IntegerField()

