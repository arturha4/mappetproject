from django.core import serializers

from users.models import MyCustomUser,Profile


def create_user(request):
    data = request.POST
    email = data['email']
    password = data['password']
    first_name = data['first_name']
    second_name = data['second_name']
    birthday = data['birthday']
    MyCustomUser.objects.create_user(email, password, first_name, second_name, birthday)


def get_json_user_profiles():
    return serializers.serialize("json", Profile.objects.all())