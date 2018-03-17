from django.conf.urls import url, include 
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from asignacionHistorias import views
from rest_framework_swagger.views import get_swagger_view
router = DefaultRouter()
print(type(views.AsignacionPorHorasView))
router.register(r'historiaDetalle', views.HistoriaDetalle.as_view(), base_name='que')
router.register(r'generarAsignacionSimple', views.AsignacionPorHorasView.as_view(), base_name='generarAsignacionSimple')

schema_view = get_swagger_view(title='API asignación de historias')
urlpatterns = [
    url(r'^$', schema_view, name = "swagger_api_view"),
    url(r'^', include(router.urls)),
    url(r'^generarAsignacionSimple/', views.AsignacionPorHorasView.as_view(),  name = 'generarAsignacionSimple'),
     
     
     
    #url(r'^obtenerAsignacion/', views.asignacionHistorias,  name = 'obtenerAsignacion'),
    url(r'^historias/(?P<pk>[0-9]+)/$', views.HistoriaDetalle.as_view(), name = 'historiaDetalle'),
    url(r'^historias/', views.HistoriaListado.as_view(), name = 'historiaListado'),
    url(r'^historiasSimples/', views.HistoriaSimpleCrear.as_view(), name = 'historiaSimpleCrear'),
    url(r'^proyectoAgil/(?P<pk>[0-9]+)/$', views.ProyectoAgilDetalle.as_view(), name = 'proyectoAgilDetalle'),
    url(r'^proyectoAgil/', views.ProyectoAgilListado.as_view(), name = 'proyectoAgilListado'),
    url(r'^desarrollador/(?P<pk>[0-9]+)/$', views.DesarrolladorDetalle.as_view(), name = 'desarrolladorAgilDetalle'),
    url(r'^desarrollador/', views.DesarrolladorListado.as_view(), name = 'desarroladorAgilListado'),
    
]
