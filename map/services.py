import json

from map.models import Point,PointComment
from django.core import serializers

def create_point(request):
    data=request.POST
    creator_id=request.user.id
    name=data['name']
    address=data['address']
    type=data['type'][0]
    latitude=data['lat']
    longitude=data['lng']
    description=data['description']
    Point.objects.create(name=name,type=type,latitude=latitude,longitude=longitude,description=description,created_by_id=creator_id,address=address)


def create_comment(request):
    try:
        comment,point_id=request.POST['comment'],request.POST['point_id']
        point=Point.objects.get(id=point_id)
        PointComment.objects.create(text=comment,point_id=point,author=request.user)
    except:
        data=json.loads(request.body)
        ax_comment,ax_point_id=data["comment"],data["point_id"]
        point = Point.objects.get(id=ax_point_id)
        PointComment.objects.create(text=ax_comment,point_id=point,author=request.user)


def get_json_point_comments():
    return serializers.serialize("json", PointComment.objects.all())

'''Возвращает  все точки'''
def get_points():
    return Point.objects.all()

