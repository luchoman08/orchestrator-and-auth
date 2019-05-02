
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('uniquecostassign/', views.generar_asignacion, name='generarAsignacion'),
    path('attributeassign/', views.generate_assignment_with_attributes, name='generate_assignment_with_attributes'),
    path('pairassign/', views.generate_pair_assignment, name='pairassign'),
    path('makepairs/', views.generate_pairs, name='makepairs'),
    re_path(r'^projects|userstories|sprints|developers$', views.general_project_management, name='generarAsignacionSimple'),
]
