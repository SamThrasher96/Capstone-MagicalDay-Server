from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hired_on = models.DateField()
    location = models.ForeignKey("Location", on_delete=models.CASCADE)