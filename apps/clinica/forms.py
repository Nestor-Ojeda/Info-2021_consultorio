from django import forms
from .models import Persona, ObraSocial

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['dni', 'nombre', 'apellido', 'fecha_nac', 'telefono']
        labels = {
        	'dni': 'Ingrese el DNI',
            'nombre': 'Ingrese el/los nombres ',
            'apellidos': 'Ingrese el/los apellidos',
            'fecha_nac': 'Ingrese fecha de Nacimiento',
            'telefono': 'Ingrese un número de teléfono',
        }
        widgets = {
        	'dni': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el número del DNI',
                    'id': 'dni'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el/los nombres que figura en DNI',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el/los apellidos como figura en DNI',
                    'id': 'apellido'
                }
            ),
            'fecha_nac': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la fecha de Nacimiento. Por Ejemplo: "16/02/1990"',
                    'id': 'fecha_nac'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un número de teléfono s/n 0 ni el 15',
                    'id': 'telefono'
                }
            ),
        }


class ObraSocialForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = ['nombre_os', 'plan_cobertura']
        labels = {
            'nombre_os': 'Obra Social',
            'plan_cobertura': 'Plan de Cobertura',
        }
        widgets = {
            'nombre_os': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de la Obra Social',
                    'id': 'nombre_os'
                }
            ),
            'plan_cobertura': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el plan de cobertura',
                    'id': 'plan_cobertura'
                }
            ),
        }