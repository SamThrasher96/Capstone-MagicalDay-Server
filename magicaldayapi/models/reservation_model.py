from django.db import models

class Reservation(models.Model):
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    guest = models.ForeignKey("Guest", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
