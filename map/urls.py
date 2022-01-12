from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('map',views.map),
    path('addpoint', views.AddPointView.as_view()),
]
