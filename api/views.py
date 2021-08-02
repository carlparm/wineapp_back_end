from django.shortcuts import render, HttpResponse
from rest_framework import serializers
from .models import Wine
from .serializers import WineSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
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

@csrf_exempt
def wine_details(request, pk):
    try:
        wine = Wine.objects.get(pk=pk)

    except Wine.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WineSerializer(wine)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WineSerializer(wine, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        wine.delete()
        return HttpResponse(status=204)