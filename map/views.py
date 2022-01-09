from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required(login_url='login')
def map(request):
    firstname,secondname=request.user.first_name,request.user.second_name
    return render(request, template_name='map/map.html',context={"fname":firstname,"sname":secondname})
