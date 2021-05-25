from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Paises, Provincia, Ciudad, Direccion)
class DireccionesAdmin(admin.ModelAdmin):
	pass