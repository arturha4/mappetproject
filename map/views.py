from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .services import create_point,get_points

@login_required(login_url='login')
def map(request):
    points=get_points()
    firstname,secondname=request.user.first_name,request.user.second_name
    return render(request, template_name='map/map.html',context={"fname":firstname,"sname":secondname,"points":points})


class AddPointView(FormView):
    def post(self, request, *args, **kwargs):
        create_point(request)
        return redirect('/map')


    def get(self, request, *args, **kwargs):
        return render(request,'map/map.html',context={"url":'addpoint'})