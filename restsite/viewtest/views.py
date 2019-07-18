from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
# Create your views here.
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

