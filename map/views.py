# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from django.views.generic import FormView
# from .serializers import PointListSerializer
# from .models import Point
# from .services import create_point,get_points, create_comment
#
#
# @login_required(login_url='login')
# def map(request):
#     points=get_points()
#     firstname,secondname=request.user.first_name,request.user.second_name
#     return render(request, template_name='map/map.html',context={"fname":firstname,"sname":secondname,"points":points})
#
#
# # class PointListView(APIView):
# #     '''Вывод списка точек'''
# #     def get(self,request):
# #         if request.user.is_authenticated:
# #             points=Point.objects.all()
# #             serializer=PointListSerializer(points,many=True)
# #             return Response(serializer.data)
# #         return Response(status=400,data={'status':'Error1'})
#
#
# class AddPointView(FormView):
#     def post(self, request, *args, **kwargs):
#         try:
#             create_point(request)
#             return redirect('/')
#         except:
#             return redirect("/")
#
#     def get(self, request, *args, **kwargs):
#         return render(request,'map/map.html',context={"url":'addpoint'})
#
#
# class AddCommentView(FormView):
#     def post(self,request,*args,**kwargs):
#         create_comment(request)
#         return redirect('/')
#
