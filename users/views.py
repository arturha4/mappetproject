import django
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from datetime import date

from users.services import create_user


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/map')
        messages.error(request, "Пользователя с такими данными не существует")
        return redirect('/login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/map')
        return render(request, 'users/login.html')


class RegistrationView(FormView):
    template_name = "users/registration.html.html"
    success_url = "/login"

    def post(self, request, *args, **kwargs):
        try:
            create_user(request)
            return redirect('/map')
        except django.db.utils.IntegrityError:
            messages.info(request, 'Пользователь с такой почтой уже существует')
            return redirect('/registration')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/map')
        return render(request, 'users/registration.html',context={'current_time': date.today().strftime("%Y-%m-%d")})


@login_required(login_url='login')
def home_page(request):
    return render(request, 'users/home.html')


@login_required(login_url='login')
def userlogout(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render

# Create your views here.
