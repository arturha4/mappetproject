from django.urls import path, include
from . import views
from users.views import CustomLoginView

urlpatterns=[
    path('login',CustomLoginView.as_view(),name='login'),
    path('registration',views.RegistrationView.as_view(),name='registration'),
    path('logout',views.userlogout,name='logout'),
]
