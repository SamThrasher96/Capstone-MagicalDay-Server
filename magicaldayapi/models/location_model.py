from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=150)
    image = models.URLField(max_length=500)  
    capacity = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    description = models.TextField(max_length=500) 