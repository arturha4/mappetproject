from django.db import models

class Point(models.Model):
    name=models.TextField()
    description=models.TextField()
    type=models.TextField()
    latitude=models.FloatField()#широта
    longitude=models.FloatField()#долгота

    def __str__(self):
        return self.name