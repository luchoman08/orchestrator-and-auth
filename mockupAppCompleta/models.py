from django.db import models

from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class Historias(models.Model):
    """
    Almacena una historia de usuario
    """
    nombre = models.CharField(_('Nombre de historia de usuario'), max_length=50, blank=False, null=False)   
    puntuacionGeneral = models.IntegerField(_('Puntuación general'), blank=False, null=False,default=0)
    fechaRegistro = models.DateTimeField(_('Fecha de registro'), auto_now=True )
    fechaMoficacion = models.DateTimeField(_('Fecha de modificacion'), auto_now=False)
    readonly_fields=('fechaRegisro' )

class Desarrollador(models.Model):
    """
    Almacena la información basica de un desarrollador
    """
    nombre = models.CharField(_('Nombre del desarrollador'), max_length = 50, blank=False, null = False)
    fechaRegistro = models.DateTimeField(_('Fecha de registro'), auto_now=True )
    fechaMoficacion = models.DateTimeField(_('Fecha de modificacion'), auto_now=False)
    readonly_fields=('fechaRegisro' )
    
