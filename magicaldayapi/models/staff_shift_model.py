from django.db import models

class StaffShift(models.Model):
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()