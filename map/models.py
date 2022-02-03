from django.db import models
from django.utils import timezone
from mappetproject import settings

'''Модель точки'''
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

'''Модель комментария'''
class Comment(models.Model):
    text=models.TextField()
    author_id=models.CharField(max_length=30)
    point_id=models.ForeignKey(Point, on_delete=models.CASCADE, default=None,related_name='comments')
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
    class Meta:
        ordering=('created_at',)
