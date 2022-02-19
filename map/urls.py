from django.urls import path
from map import views


urlpatterns = [
    path('',views.map),
    path('addpoint', views.AddPointView.as_view()),
    path('addcomment',views.AddCommentView.as_view()),
]
