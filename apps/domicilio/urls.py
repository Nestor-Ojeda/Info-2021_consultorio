from django.urls import path
from .views import CrearDireccion, ListadoDireccion

urlpatterns = [
    path('crear_domicilio/', CrearDireccion.as_view(), name='crear_domicilio'),
    path('listar_domicilio/', ListadoDireccion.as_view(), name='listar_domicilio'),

]
