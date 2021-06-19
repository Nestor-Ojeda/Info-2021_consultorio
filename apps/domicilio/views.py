from django.shortcuts import render, redirect
from .models import Direccion
from .forms import DireccionForm

from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CrearDireccion(CreateView):
    model = Direccion
    form_class = DireccionForm
    template_name = 'domicilio/crear_domicilio.html'
    success_url = reverse_lazy('domicilio:listar_domicilio')

class ListadoDireccion(ListView):
    model = Direccion
    template_name = 'domicilio:listar_domicilio.html'
    context_object_name = 'direccion' #cambial de object_list a direccion
    queryset = Direccion.objects.filter(estado = True) 

class ActualizarDireccion(UpdateView):
    model = Direccion
    template_name = 'domicilio/editar_domicilio.html'
    form_class = DireccionForm
    success_url = reverse_lazy('domicilio:listar_domicilio')

class EliminarDireccion(DeleteView):
    model = Direccion

    def post(self, request, pk, *args, **kwargs):
        object = Direccion.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('domicilio:listar_domicilio')