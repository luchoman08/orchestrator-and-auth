from django.urls import path
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from asignacionHistorias import views
from rest_framework_swagger.views import get_swagger_view
router = DefaultRouter()

schema_view = get_swagger_view(title='API asignación de historias')
urlpatterns = [
    path('asignacionsimple/', views.AsignacionPorHorasView.as_view(),  name = 'asignacionsimple'),
    path('generarAsignacionPorCaracteristicas/', views.AsignacionPorCaractericasView.as_view(),  name = 'generarAsignacionPorCaracteristicas'),
    path('generarAsignacionGruposHistorias/', views.AsignacionPorCaracteristicasYGruposView.as_view(), name = 'generarAsignacionGruposHistorias'),
]
