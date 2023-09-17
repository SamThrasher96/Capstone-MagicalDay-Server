from django.db import models

class ShowDetails(models.Model):
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    duration = models.IntegerField()
    cast_size = models.IntegerField()
    running = models.BooleanField()

    @property
    def show_name(self):
        return self.location.name

    @property
    def show_image(self):
        return self.location.image

    @property
    def show_description(self):
        return self.location.description

    @property
    def show_open(self):
        return self.location.opening_time 

    @property
    def show_close(self):
        return self.location.closing_time