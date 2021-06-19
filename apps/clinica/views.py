from django.shortcuts import render, redirect
from .models import Persona, ObraSocial
from .forms import PersonaForm, ObraSocialForm
# Create your views here.

from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

class Inicio(TemplateView):
    template_name = 'index.html'

#----------CRUD de Persona----------------

class CrearPersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'clinica/crear_persona.html'
    success_url = reverse_lazy('clinica:listar_persona')

class ListadoPersona(ListView):
    model = Persona
    template_name = 'clinica/listar_persona.html'
    context_object_name = 'persona' #cambial de object_list a autores
    queryset = Persona.objects.filter(estado = True) 

class ActualizarPersona(UpdateView):
    model = Persona
    template_name = 'clinica/editar_persona.html'
    form_class = PersonaForm
    success_url = reverse_lazy('clinica:listar_persona')

class EliminarPersona(DeleteView):
    model = Persona

    def post(self, request, pk, *args, **kwargs):
        object = Persona.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('clinica:listar_persona')

#----------CRUD Obra Social-----------------

class CrearObraSocial(CreateView):
    model = ObraSocial
    form_class = ObraSocialForm
    template_name = 'clinica/crear_obra_social.html'
    success_url = reverse_lazy('clinica:listar_obra_social')

class ListadoObraSocial(ListView):
    model = ObraSocial
    template_name = 'clinica/listar_obra_social.html'
    context_object_name = 'obra_social' #cambial de object_list a obra_social
    queryset = ObraSocial.objects.filter(estado = True) 

class ActualizarObraSocial(UpdateView):
    model = ObraSocial
    template_name = 'clinica/editar_obra_social.html'
    form_class = ObraSocialForm
    success_url = reverse_lazy('clinica:listar_obra_social')

class EliminarObraSocial(DeleteView):
    model = ObraSocial

    def post(self, request, pk, *args, **kwargs):
        object = ObraSocial.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('clinica:listar_obra_social')

# ------------------Crud         ----------------------------
class CrearObraSocial(CreateView):
    model = ObraSocial
    form_class = ObraSocialForm
    template_name = 'clinica/crear_obra_social.html'
    success_url = reverse_lazy('clinica:listar_obra_social')

class ListadoObraSocial(ListView):
    model = ObraSocial
    template_name = 'clinica/listar_obra_social.html'
    context_object_name = 'obra_social' #cambial de object_list a obra_social
    queryset = ObraSocial.objects.filter(estado = True) 

class ActualizarObraSocial(UpdateView):
    model = ObraSocial
    template_name = 'clinica/editar_obra_social.html'
    form_class = ObraSocialForm
    success_url = reverse_lazy('clinica:listar_obra_social')

class EliminarObraSocial(DeleteView):
    model = ObraSocial

    def post(self, request, pk, *args, **kwargs):
        object = ObraSocial.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('clinica:listar_obra_social')