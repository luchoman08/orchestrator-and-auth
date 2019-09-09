from django.shortcuts import render, redirect
from gestionAplicaciones.forms import ApplicationForm
from gestionAplicaciones.models import Application
from gestionAplicaciones.manager import createApplication, generateApplicationKey
from gestionUsuarios.models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from gestionAplicaciones.start import init_permissions as ip

# Create your views here.
@login_required
def upsert_app(request, newContext={}):
    app = None
    try:
        app = Application.objects.filter(owner__username=request.user.username).get()
    except:
        pass
    
    if app and not(request.POST):
        form = ApplicationForm(instance=app)
        print(form)
    else:
        form = ApplicationForm(request.POST or None, request.FILES or None)

    context = {'form': form, 'app': app or None}
    context.update(newContext)

    def create_app(form):
        app = form.instance
        try:
            createApplication(app, request.user.username)
            return redirect('list-apps')
        except Usuario.DoesNotExist:
            return HttpResponse(status=500)

    def update_app(form):
        form.save()

    if request.method == 'POST' and form.is_valid():
        if Application.objects.filter(url=form.cleaned_data['url']).exists():
            return update_app(form)
        else:
            return create_app(form)

    return render(request, "gestionAplicaciones/upsert-application.html", context=context)

@login_required    
def init_permissions(request):
    if ip():
        return HttpResponse(status=200)

    return HttpResponse(status=500)

@login_required
def request_api_key(request, app_id):
    app = None
    try:
        app = Application.objects.filter(id=app_id).get()
    except:
        return HttpResponse(status=500)

    if app.owner.username != request.user.username:
        return HttpResponse(status=101)

    try:
        generateApplicationKey(app, "2025-11-11")
    except:
        return HttpResponse(status=500)

    return upsert_app(request   , {'message': "La API key se ha generado correctamente"})
    
        