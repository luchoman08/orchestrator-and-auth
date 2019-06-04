from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponse
import requests
import json

# Create your views here.


def proxy_request(remote_url, req, headers=None):
    http_method = req.method
    if http_method == 'POST':
        response = requests.post(remote_url, json=req.data)
    elif http_method == 'PATCH':
        response = requests.patch(remote_url, json=req.data, params=reg.GET, headers=headers)
    elif http_method == 'GET':
        response = requests.get(remote_url, params=req.GET, headers=headers)
    else:
        raise Exception('El metodo http "{0}" es invalido'.format(http_method))
    print(remote_url, 'remote url')
    print(response, http_method, 'response at proxy request')
    return JsonResponse(json.loads(response.text), safe=False)


def proxy_request_to_assignment(endpoint, req, headers=None):
    remote_url = 'http://localhost:3001/' + endpoint + '/'
    return proxy_request(remote_url, req, headers)


def proxy_request_to_project_management(req):
    headers = {"Authorization":"Bearer eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjozMDM0NTZ9:1fKuoT:9O26jWVYE63vCuzbrjCsAo5nM1Y"}
    remote_url = 'http://localhost:3000' + req.path.replace('/api/v1', '')
    return proxy_request(remote_url, req, headers)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def generate_assignment_with_attributes(request):
    return proxy_request_to_assignment('attributeassign', request)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def generar_asignacion(request):
    return proxy_request_to_assignment('uniquecostassign', request)


@api_view(['POST'])
@permission_classes((AllowAny,))
def generate_group_assignment(request):
    return proxy_request_to_assignment('groupassign', request)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def generate_pair_assignment(request):
    return proxy_request_to_assignment('pairassign', request)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def generate_pairs(request):
    return proxy_request_to_assignment('makepairs', request)


@api_view(['GET', 'PATCH'])
@permission_classes((AllowAny, ))
def general_project_management(req):
    return proxy_request_to_project_management(req)
