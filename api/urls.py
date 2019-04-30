
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^uniquecostassign/', views.generar_asignacion, name='generarAsignacion'),
    url(r'^attributeassign/', views.generate_assignment_with_attributes, name='generate_assignment_with_attributes'),
    url(r'^pairassign/', views.generate_pair_assignment, name='pairassign'),
    url(r'^makepairs/', views.generate_pairs, name='makepairs'),
    url(r'^projects|userstories|sprints|developers$', views.general_project_management, name='generarAsignacionSimple'),
]
