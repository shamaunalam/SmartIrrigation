from django.db import models

# Create your models here.
class DeviceStatus(models.Model):
    device_id = models.TextField(max_length=20,primary_key=True)
    temp   = models.FloatField(default=0.0)
    humid  = models.FloatField(default=0.0)
    moist  = models.FloatField(default=0.0)
    switch = models.IntegerField(default=0,choices=((0,0),(1,1))) 
    def __str__(self):
        return self.device_id
    