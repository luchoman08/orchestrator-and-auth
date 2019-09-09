from django.urls import path, include
from gestionAplicaciones import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', views.upsert_app, name = 'upsert-app'),
    path('list-apps', views.upsert_app, name = 'list-apps'),
    path('generate-api-key/<int:app_id>', views.request_api_key, name = 'generate-api-key'),
    path('api', schema_view, name="api"),
    path('init', views.init_permissions, name="init-permissions")
]
