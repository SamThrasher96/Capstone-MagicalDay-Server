from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    image = models.CharField(max_length=500)
    opening_time = models.TimeField()
    closing_time = models.TimeField()