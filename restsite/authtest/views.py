from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import AuthModelSerializers
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import *
# Create your views here.
class AuthModelViewSet(viewsets.ModelViewSet):
    # 添加授权之后如果没有登录 则只能只读模式
    # 登录之后可以 post创建对象  当时想要修改对象则必须保证该对象为当前用户创建的
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    queryset = AuthModel.objects.all()
    serializer_class = AuthModelSerializers
