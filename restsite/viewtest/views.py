from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
# Create your views here.

"""
使用高级混合类
"""
class ViewModelListMixinView(generics.ListCreateAPIView,):
    queryset = ViewModel.objects.all()
    serializer_class = ViewModelSerializers

class ViewModelDetailMixinView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ViewModel.objects.all()
    serializer_class = ViewModelSerializers



"""
使用混合类
"""
# class ViewModelListMixinView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = ViewModel.objects.all()
#     serializer_class = ViewModelSerializers
#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class ViewModelDetailMixinView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = ViewModel.objects.all()
#     serializer_class = ViewModelSerializers
#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self,request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



"""
基于类视图
"""
class ViewModelListView(APIView):
    def get(self,request):
        serializers = ViewModelSerializers(ViewModel.objects.all(),many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializers = ViewModelSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ViewModelDetailView(APIView):
    def get(self,request,id):
        viewmodel = get_object_or_404(ViewModel,pk=id)
        serializers = ViewModelSerializers(viewmodel)
        return Response(serializers.data)
    def put(self,request,id):
        viewmodel = get_object_or_404(ViewModel,pk=id)
        serializers = ViewModelSerializers(viewmodel,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        viewmodel = get_object_or_404(ViewModel,pk=id)
        viewmodel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










"""
基于视图函数
"""


@api_view(["GET","POST"])
def viewmodelslist(request,format=None):
    if request.method == "GET":
        serializers = ViewModelSerializers(ViewModel.objects.all(),many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializers = ViewModelSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","PATCH","DELETE"])
def viewmodeldetail(request,id,format=None):
    viewmodel = get_object_or_404(ViewModel,pk=id)
    if request.method == "GET":
        serializers = ViewModelSerializers(viewmodel)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        serializers = ViewModelSerializers(viewmodel,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        get_object_or_404(ViewModel,pk=id).delete()
        return Response(status.HTTP_204_NO_CONTENT)

