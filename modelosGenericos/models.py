from django.db import models

# Create your models here.

class Observable(models.Model):
    fechaRegistro = models.DateTimeField(_('Fecha de registro'), auto_now=True )
    