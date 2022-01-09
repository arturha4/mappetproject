from django.db import models

class Point(models.Model):
    name=models.TextField()
    description=models.TextField()
    type=models.TextField()
    latitide=models.FloatField()#y
    longitude=models.FloatField()#x

    def __str__(self):
        return self.name