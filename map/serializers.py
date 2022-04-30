from rest_framework import serializers
from rest_framework import permissions

from .models import Point


class PointListSerializer(serializers.ModelSerializer):
    '''Список точек'''

    def get_username(self, obj):
        return obj.created_by.first_name+' '+ obj.created_by.second_name

    created_by = serializers.SerializerMethodField("get_username")

    class Meta:
        model=Point
        fields="__all__"
        permission_classes=[permissions.IsAuthenticated]


class PointDetailSerializer(serializers.ModelSerializer):
    '''Информация о точке'''
    created_by = serializers.SerializerMethodField("get_username")
    class Meta:
        model=Point
        fields="__all__"