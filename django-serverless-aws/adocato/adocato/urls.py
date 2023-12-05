"""
URL configuration for adocato project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.views import RacaListCreate, RacaRetrieveUpdateDestroy, UsuarioListCreate, UsuarioRetrieveUpdateDestroy, GatoListCreate, GatoRetrieveUpdateDestroy, AdocaoListCreate, AdocaoRetrieveUpdateDestroy

schema_view = get_schema_view(
   openapi.Info(
      title="Adocato API",
      default_version='v1',
      description="API Adocato",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="andre.almeida@escolar.ifrn.edu.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path('api/usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('api/usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view(), name='usuario-retrieve-update-destroy'),
    path('api/gatos/', GatoListCreate.as_view(), name='gato-list-create'),
    path('api/gatos/<int:pk>/', GatoRetrieveUpdateDestroy.as_view(), name='gato-retrieve-update-destroy'),
    path('api/adocoes/', AdocaoListCreate.as_view(), name='adocao-list-create'),
    path('api/adocoes/<int:pk>/', AdocaoRetrieveUpdateDestroy.as_view(), name='adocao-retrieve-update-destroy'),
    path('api/racas/', RacaListCreate.as_view(), name='raca-list-create'),
    path('api/racas/<int:pk>/', RacaRetrieveUpdateDestroy.as_view(), name='raca-retrieve-update-destroy'),
]
