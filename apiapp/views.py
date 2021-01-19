from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apiapp.filter import ComputerFilterSet
from apiapp.models import Computer
from apiapp.paginat import MyPageNumber, MyCursorPagination, MyLimitOffsetPagination
from apiapp.serializer import ComputerModelSerializer
from apiapp.thorttle import MyThrottle


class UserAPIView(APIView):
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response("OK")

    def post(self, request):
        return Response("写")


class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer
    # filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # search_fields = ["name", "price"]

    # 指定排序的条件
    ordering = ["price"]
    # 查询价格大于3000小于9000的电脑
    filter_class = ComputerFilterSet

    # 分页
    pagination_class = MyPageNumber
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination

