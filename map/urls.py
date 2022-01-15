from django.urls import path
from map import views


urlpatterns = [
    path('map',views.map),
    path('addpoint', views.AddPointView.as_view()),
]
