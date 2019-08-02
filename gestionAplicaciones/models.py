from django.db import models
from django.utils.translation import ugettext as _
from gestionUsuarios.models import Usuario
# Create your models here.

class ApplicationKey(models.Model):
    key = models.CharField(_('Applicatin key'), null=False,  max_length=150)
    creationDate = models.DateTimeField(_('Creation date'), auto_now=True)
    expirationDate = models.DateTimeField(_('Fecha de expiración'), null=False)

class Application(models.Model):
    name = models.CharField(_('Nombre de la aplicación'), null=False,  max_length=20)
    description = models.TextField(_('Descripción de la aplicación'), max_length=100)
    owner = models.OneToOneField(to=Usuario, on_delete=models.CASCADE, related_name='owner')
    key = models.OneToOneField(to=ApplicationKey, on_delete=models.CASCADE, related_name='owner')
