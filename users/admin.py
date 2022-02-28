from django.contrib import admin
from .models import MyCustomUser,Profile

admin.site.register(MyCustomUser)
admin.site.register(Profile)
