from django.db import models
from django.utils.translation import ugettext as _
from mockupAppCompleta import models as models_mockup
# Create your models here.


class Atributo(models.Model):
    """
    Atributo o cualidad medible en un ente
    """
    nombre = models.CharField(_('Nombre del atributo'), max_length = 50, blank=False, null = False)
    descripcion = models.CharField(_('Nombre del atributo'), max_length = 50, blank=False, null = False)
    fechaRegistro = models.DateTimeField(_('Fecha de registro'), auto_now=True )
    
class HistoriaAsignacion(models_mockup.Historias):
    atributos = models.ManyToManyField(Atributos,related_name='HistoriaAsignacionAtributos' )

class DesarrolladorAsignacion(models_mockup.Historias):
    atributos = models.ManyToManyField( Atributos,related_name='DesarrolladorAsignacionAtributos')

class PuntuacionAtributo(models.Model):
    