from .models import Application, ApplicationKey
from gestionUsuarios.models import Usuario
import uuid
def createApplication(application, ownerUserName):
    '''
    Create an application with owner
    application: Application
    ownerUserName: string
    '''
    try:
        owner = Usuario.objects.filter(username=ownerUserName).get()
    except Usuario.DoesNotExist:
        raise Usuario.DoesNotExist
    application.owner = owner
    return application.save()

def generateApplicationKey(application, expirationDate):
    '''
    Generate an app API key
    application: Application
    expirationDate: Date
    '''
    uniqueID = uuid.uuid4()
    appKey = ApplicationKey(key=uniqueID, expirationDate=expirationDate)
    appKey.save()
    application.key = appKey
    application.save()
