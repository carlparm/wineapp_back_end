from django.shortcuts import render, HttpResponse
from rest_framework import serializers
from .models import Wine
from .serializers import WineSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def wine_list(request):
    if request.method == 'GET':
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def wine_details(request, pk):
    try:
        wine = Wine.objects.get(pk=pk)

    except Wine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WineSerializer(wine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WineSerializer(wine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        wine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)