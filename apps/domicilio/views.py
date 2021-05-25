from django.shortcuts import render
from .models import Direccion
# Create your views here.
def direcciones(request):
    lista_domicilios = Direccion.objects.all()
    return render(request, "domicilio/domicilio.html",{"lista_domicilios":lista_domicilios})
