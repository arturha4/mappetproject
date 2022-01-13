from map.models import Point

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

'''Возвращает  все точки'''
def get_points():
    return Point.objects.all()

print(get_points())
