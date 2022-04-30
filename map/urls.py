from django.urls import path
from . import views


urlpatterns = [
    path('',views.map),
    path('addpoint', views.AddPointView.as_view()),
    path('addcomment',views.AddCommentView.as_view()),
    path("points/", views.PointListView.as_view())
]
