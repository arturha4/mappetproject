from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView


@login_required(login_url='login')
def map(request):
    firstname,secondname=request.user.first_name,request.user.second_name
    return render(request, template_name='map/map.html',context={"fname":firstname,"sname":secondname})


class AddPointView(FormView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        return redirect('/map')


    def get(self, request, *args, **kwargs):
        return render(request,'map/map.html',context={"url":'addpoint'})