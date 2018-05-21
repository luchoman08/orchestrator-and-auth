from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponse
import requests
import json

# Create your views here.
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def generarAsignacion(request, format=None):        
    remoteurl = 'http://task-assignment:8001/api/v1/asignacionsimple/'
    response = requests.post(remoteurl, json=request.data)
    return JsonResponse(json.loads(response.text))

@api_view(['GET'])
@permission_classes((AllowAny, ))
def gestionGeneralProyectos(req, format=None):        
    remoteurl = 'http://project-managers-interface:3000' + req.path.replace('/api/v1', '')
    response = requests.get(remoteurl,  params = req.GET)
    return JsonResponse(json.loads(response.text),  safe=False, status=response.status_code)