from django.db import models

class StaffShift(models.Model):
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()