from map.models import Point,PointComment

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
    comment,point_id=request.POST['comment'],request.POST['point_id']
    point=Point.objects.get(id=point_id)
    PointComment.objects.create(text=comment,point_id=point,author=request.user)



'''Возвращает  все точки'''
def get_points():
    return Point.objects.all()

