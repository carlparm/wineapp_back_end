from django.shortcuts import render, HttpResponse
from rest_framework import serializers
from .models import Wine
from .serializers import WineSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

def wine_list(request):
    if request.method == 'GET':
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

