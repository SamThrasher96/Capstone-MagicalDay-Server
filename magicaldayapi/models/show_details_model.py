from django.db import models

class ShowDetails(models.Model):
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    duration = models.IntegerField()
    cast_size = models.IntegerField()
    running = models.BooleanField()