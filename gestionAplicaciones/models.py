from django.db import models
from django.utils.translation import ugettext as _
from gestionUsuarios.models import Usuario
# Create your models here.

class ApplicationKey(models.Model):
    key = models.CharField(_('API key'), null=False,  max_length=150)
    creationDate = models.DateTimeField(_('Fecha de creación'), auto_now=True)
    expirationDate = models.DateTimeField(_('Fecha de expiración'), null=False)

class AppPermission(models.Model):
    name = models.CharField(_("Nombre de el permiso"), null=False, max_length=25)
    crated_date = models.DateField(_("Fecha de creación de permiso"), auto_now=True)
    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(_('Nombre de la aplicación'), null=False,  max_length=20, unique=True)
    description = models.TextField(_('Descripción de la aplicación'), max_length=100, null=False)
    owner = models.OneToOneField(to=Usuario, on_delete=models.CASCADE, related_name='owner')
    url = models.URLField(_('URL de la aplicación'), null=False, unique=True)
    key = models.OneToOneField(to=ApplicationKey, on_delete=models.CASCADE, related_name='app_key', unique=True, null=True, blank=True)
    associated_users = models.ManyToManyField(Usuario, related_name="application_associated_user")
    taiga_key = models.CharField(_("Taiga API key"), max_length=50,  blank=True)
    permissions = models.ManyToManyField(AppPermission, related_name="app_permissions")