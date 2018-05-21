from rest_framework import serializers
from django.utils.translation import ugettext as _
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(label='Nombre Completo', required = True, max_length = 150)
    email = serializers.EmailField(label = 'Email', required = True)
    class Meta:
        model = Usuario
        fields =  ['username', 'first_name', 'email','password']
    