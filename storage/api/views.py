from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework import generics


# Create your views here.


@api_view(['GET'])
def getLocation(request):
    location = Location.objects.all()
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addLocation(request):
    serializer = LocationSerializer(data=request.data)
    if Location.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'payload':serializer.error,'messge':'wrong'})
    return Response(serializer.data)


# def showLocation(request):
#     resultapi = request.get('http://127.0.0.1:8000/getLocation')
#     jsonobj = resultapi.json()
#     return render(request,'index.html',("Location":jsonobj))


# @api_view(['POST'])
# class LocationCreateApi(generics.CreateAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer




# api_view(['GET','POST'])
# def getLocation(request):
#     if request.method == 'GET':
#         location = Location.objects.all()
#         serializer = LocationSerializer(location, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)


@api_view(['GET'])
def getItem(request):
    item = Item.objects.all()
    serializer = ItemSerializer(item, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteLocation(request, pk):
    location = Location.objects.get(id=pk)
    location.delete()
    return Response("location deleted")


@api_view(['PUT'])
def updateLocation(request, pk):
    location = Location.objects.get(id=pk)
    serializer = LocationSerializer(instance=location, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    
