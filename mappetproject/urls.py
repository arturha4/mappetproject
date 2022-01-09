from django.contrib import admin
from django.urls import path, include
import map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('',include('map.urls')),

]
