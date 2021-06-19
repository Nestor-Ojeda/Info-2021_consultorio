from django import forms
from .models import Paises, Provincia, Ciudad, Direccion



class PaisesForm(forms.ModelForm):
    class Meta:
        model = Paises
        fields = ['codigo', 'pais']
        labels = {
        	'codigo': 'Ingrese el codigo ',
            'pais': 'Ingrese el país ',
        }
        widgets = {
        	'codigo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el codigo de letras perteneciente al pais, por ejemplo, "AR"',
                    'id': 'codigo'
                }
            ),
            'pais': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del País',
                    'id': 'pais'
                }
            ),
            
        }


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['pais', 'nombre']
        labels = {
        	'pais': 'Ingrese el Pais',
            'nombre': 'Ingrese la Provincia',
        }
        widgets = {
        	'pais': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el país',
                    'id': 'pais'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de la Provincia',
                    'id': 'nombre'
                }
            ),
        }

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['provincia', 'cod_Postal', 'nom_ciudad']
        labels = {
        	'provincia': 'Provincia',
            'cod_Postal': 'Codigo Postal ',
            'nom_ciudad': 'Ciudad',

        }
        widgets = {
        	'provincia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de la Provincia',
                    'id': 'provincia'
                }
            ),
            'cod_Postal': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el Codigo Postal',
                    'id': 'cod_postal'
                }
            ),
            'nom_ciudad': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de la Ciudad',
                    'id': 'nom_ciudad'
                }
            ),  
        }


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['ciudad', 'barrio', 'calle', 'numero', 'nota']
        labels = {
        	'ciudad': 'Ciudad',
            'barrio': 'Barrio ',
            'calle': 'Calle',
            'numero': 'Numero',
            'nota': 'Nota',
        }
        widgets = {
        	'ciudad': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la ciudad',
                    'id': 'ciudad'
                }
            ),
            'barrio': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el barrio ',
                    'id': 'barrio'
                }
            ),
            'calle': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la calle',
                    'id': 'calle'
                }
            ),
            'numero': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el numero de la casa',
                    'id': 'numero'
                }
            ),
            'nota': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un nota adicional',
                    'id': 'nota'
                }
            ),
        }
