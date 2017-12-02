from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from modelamientoAsignaciones import fabricaModelosLineales as fml
from modelamientoAsignaciones import asignacion
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def asignacionHistorias(request):
    historias = HistoriaAsignacion.objects.all()
    desarrolladores = DesarrolladorAsignacion.objects.all()
    asignacionObj = asignacion.ModeloAsignaciones(desarrolladores, historias,  asignacion.TipoAsignacion.sencilla)
    modelo_lineal_simple = fml.FabricaModeloLinealUnicaPonderacion(asignacionObj)
    print(modelo_lineal_simple.restriccionesEquilibrioAsignacion())

    return HttpResponse(
        "Hasta si, promedio = " + str(asignacionObj.promedioPuntos)
        +
        "Hasta si, cantidad desarrolladores = " + str(asignacionObj.cantidadDesarrolladores)+
        "Hasta si, cantidad historias = " + str(asignacionObj.cantidadHistorias))