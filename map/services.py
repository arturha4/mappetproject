from .models import Point

#добавить адрес
def create_point(request):
    data=request.POST
    creator_id=request.user.id
    name=data['name']
    address=data['address']
    type=data['type'][0]
    latitude=data['lat']
    longitude=data['lng']
    Point.objects.create(name=name,type=type,latitude=latitude,longitude=longitude,description='Добавьте ваше описание',created_by_id=creator_id,address=address)