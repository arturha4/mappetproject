from .models import Point


def create_point(request):
    data=request.POST
    name=data['name']
    address=data['address']
    type=data['type'][0]
    latitude=data['lat']
    longitude=data['lng']
    Point.objects.create()