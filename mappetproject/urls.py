from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import map
from mappetproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('',include('map.urls')),
    path('vue/',include('vue.urls'))
]
