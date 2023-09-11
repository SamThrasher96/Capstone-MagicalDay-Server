from django.db import models

class RideDetails(models.Model):
    operating = models.BooleanField()
    height_requirement = models.IntegerField()
    duration = models.IntegerField()
    description = models.CharField(max_length=500)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    expected_wait_time = models.IntegerField()

