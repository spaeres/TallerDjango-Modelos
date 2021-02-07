from django.db import models
from measurements.models import Measurement


# Create your models here.
class Alarm(models.Model):
    name = models.CharField(max_length=50, default=None)
    measurements = models.ManyToManyField(Measurement)

    def __str__(self):
        return '{}'.format(self.name)


