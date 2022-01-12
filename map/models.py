from django.db import models

from mappetproject import settings


class Point(models.Model):
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    address=models.TextField()
    name=models.TextField()
    description=models.TextField()
    type=models.TextField()
    latitude=models.FloatField()#широта
    longitude=models.FloatField()#долгота

    def __str__(self):
        return self.name