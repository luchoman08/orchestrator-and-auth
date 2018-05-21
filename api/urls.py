
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^uniquecostassign/', views.generarAsignacion, name = 'generarAsignacionSimple'),
    url(r'^projects|userstories|sprints|developers$', views.gestionGeneralProyectos, name = 'generarAsignacionSimple'),
]