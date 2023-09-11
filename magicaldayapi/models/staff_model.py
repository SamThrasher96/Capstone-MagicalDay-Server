from django.db import models

class Staff(models.Model):
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    hired_on = models.DateField()