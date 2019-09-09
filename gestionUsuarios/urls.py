"""asignacion_tareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework_jwt.views import obtain_jwt_token


from django.urls import path, include
from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    path('index/', views.index, name = 'gestionUsuariosIndex'),
    path('signup/', views.crearUsuarios, name = 'signup'),
    path('api/v1/signup/', views.UserCreatePublic.as_view(), name = 'sigini-api' ),
    path('signin/', views.loginInterno, name = 'signin'),
    path('logout/', views.logout_view, name = 'logout'),
    path('api/v1/auth/', obtain_jwt_token),
]
