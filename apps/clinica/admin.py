from django.contrib import admin
from .models import *

# Register your models here.

@admin.register( Paciente, ObraSocial, Odontologo, Secretaria, Turno)
class ClinicaAdmin(admin.ModelAdmin):
	pass

@admin.register(Persona)
class Persona(admin.ModelAdmin):
	list_display = ('id', 'dni', 'nombre', 'apellido', 'fecha_nac', 'telefono' )
	ordering = ('nombre',)
	search_fields = ('dni','nombre', 'apellido', 'fecha_nac', 'telefono')
	#list_editable = ('dni','nombre', 'apellido', 'fecha_nac', 'telefono') #se puede editar todos los campos
	list_display_links = ('dni', 'nombre', 'apellido')
	list_per_page = 15


@admin.register(Responsable)
class Responsable(admin.ModelAdmin):
	list_display = ('id', 'persona', 'tipo_resp' )
	ordering = ('tipo_resp',)
	search_fields = ('persona','tipo_resp')
	#list_editable = ('persona','tipo_resp') #se puede editar todos los campos
	list_display_links = ('persona', 'tipo_resp')
	list_per_page = 15
"""
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	list_display = ('id', 'coloreado', 'creditos') #pone los campos
	#ordering = ('nombre',) #ordena decreciente
	search_fields = ('nombre', 'creditos') #susca por nombres o por creditos
	#list_editable = ('nombre', 'creditos') #edita los campos pasados
	list_display_links = ('coloreado',) # Pone linhs en los nombres
	list_filter = ('creditos',) #filtra por creditos
	list_per_page = 15 #paginación
	#exclude = ('creditos',) # excluye de formulario tanto para editar como crear
	
	fieldsets = (
			(None, {
				'fields': ('nombre',)
				}),
			('Advanced options', {
				'classes': ('collapse', 'wide', 'extrapretty'),
				'fields': ('creditos', 'docente')
				})
		)
	
	def datos(self,obj):
		return obj.nombre.upper()

	datos.short_description = "CURSO (MAYÚS)"
	datos.empty_value_display = "???"
	datos.admin_order_field = 'nombre'
	"""