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
@permission_classes((AllowAny, ))
def generarAsignacion(request, format=None):        
    remoteurl = 'http://user-stories-assignment:3001/uniquecostassign/'
    print(request.data)
    response = requests.post(remoteurl, json=request.data)
    return JsonResponse(json.loads(response.text), safe=False)

@api_view(['GET', 'PATCH'])
@permission_classes((AllowAny, ))
def gestionGeneralProyectos(req, format=None):
	headers = {"Authorization":"Bearer eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjozMDM0NTZ9:1fKuoT:9O26jWVYE63vCuzbrjCsAo5nM1Y"}        
	remoteurl = 'http://project-managers-interface:3000' + req.path.replace('/api/v1', '')
	response = {}
	if req.method == 'PATCH':
		print(req.data, 'data desde python')
		response = requests.patch(remoteurl, json=req.data, params = req.GET, headers = headers)
	if req.method == 'GET':
		response = requests.get(remoteurl, params = req.GET, headers = headers)
	return JsonResponse(json.loads(response.text),  safe=False, status=response.status_code)
