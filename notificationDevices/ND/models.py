from django.db import models

class Device(models.Model):
    name = models.CharField(max_length= 100)
    deviceType = models.BooleanField()
    adress = models.CharField(max_length= 100)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    longtitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    soundRadius = models.IntegerField()