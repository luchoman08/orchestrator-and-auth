from rest_framework import serializers
from django.utils.translation import ugettext as _
from modelosGenericos import models as modelos_genericos
from .models import Historia, Desarrollador, AsignacionPorHoras
class HistoriaSerializador(serializers.ModelSerializer):
    class Meta:
        model = modelos_genericos.Historia
        fields = ('nombre', 'proyecto', 'descripcion', 'puntuacionGeneral')

class HistoriaSimpleSerializador(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['id_externo', 'puntuacionGeneral']
        
class DesarrolladorSimpleSerializador(serializers.ModelSerializer):
    class Meta:
        model = Desarrollador
        fields = ['id_externo', 'horasDisponiblesSemana']
        
class DesarrolladorSerializador(serializers.ModelSerializer):
    class Meta:
        model = modelos_genericos.Desarrollador
        fields = ('id_externo', 'horasDisponiblesSemana')

class ProyectoAgilSerializador(serializers.ModelSerializer):
    class Meta:
        model = modelos_genericos.ProyectoAgil
        fields = ('nombre', 'fechaInicio', 'fechaFinalizacion', "correspondenciaPuntosHoras")

class AsignacionPorHorasSerializer(serializers.ModelSerializer):
    desarrolladores =  DesarrolladorSimpleSerializador(many=True, required = True)
    historias =  HistoriaSimpleSerializador(many=True, required = True)
    class Meta:
        model = AsignacionPorHoras
        fields = ('historias', 'desarrolladores', 'relacion_horas_puntos' )
        
    def get_historias(self):
        historias = self.validated_data.get('historias')
        return [Historia(**historia) for historia in historias ]
    def get_desarrolladores(self):
        desarrolladores = self.validated_data.get('desarrolladores')
        return [Desarrollador(**desarrollador) for desarrollador in desarrolladores ]    
        
"""
class HistoriaSimpleSerializador(serializers.Serializer):
    id = serializers.IntegerField(label = _('Id historia'), required = True)
    puntuacion = serializers.IntegerField(label = _('Horas historia'),  min_value = 0, max_value = 168, required = True)

class DesarrolladorSerializer(serializers.Serializer):
    id = serializers.IntegerField(label = _('Id Desarrollador'),required = True)
    horas_disponibles_semana = serializers.IntegerField(label = _('Horas disponibles a la semana desarrollador'), min_value = 0, max_value = 168, required = True)



class AsignacionPorHorasSerializer(serializers.Serializer):
    desarrolladores = serializers.ListField(child = DesarrolladorSerializador(), required = True)
    historias = serializers.ListField(child = HistoriaSimpleSerializador(), required = True)
    relacion_horas_puntos = serializers.FloatField (required = True, min_value = 0, max_value = 2000)
"""    