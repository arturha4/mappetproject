from users.models import MyCustomUser


def create_user(request):
    data = request.POST
    email = data['email']
    password = data['password']
    first_name = data['first_name']
    second_name = data['second_name']
    birthday = data['birthday']
    MyCustomUser.objects.create_user(email, password, first_name, second_name, birthday)