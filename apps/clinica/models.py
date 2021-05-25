from django.db import models
from apps.domicilio.models import Direccion

# Create your models here.

class Persona(models.Model):
	dni = models.CharField(max_length= 9)
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	fecha_nac = models.DateField()
	telefono = models.CharField(max_length = 15)

	def __str__(self):
		tex = "{0} {1} {2} {3} {4}"
		return tex.format(self.dni, self.nombre, self.apellido, self.fecha_nac, self.telefono)

class Responsable(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, related_name="pers")
	tipo_resp = models.CharField(max_length=50)

	def __str__(self):
		text = "{0} {1}"
		return text.format(self.persona, self.tipo_resp)

class ObraSocial(models.Model):
	nombre_os = models.CharField(max_length= 50)
	plan_cobertura = models.CharField(max_length = 255)

	def __str__(self):
		text = "{0} {1} "
		return text.format(self.nombre_os, self.plan_cobertura)


class Paciente(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, related_name="pers1")
	tiene_OS = models.BooleanField(default=False)
	obra_social = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True, related_name="obra_social")
	tipo_sangre = models.CharField(max_length=50)
	responsable = models.ForeignKey(Responsable, on_delete=models.SET_NULL, null=True, related_name="responsable")
	domicilio = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, related_name="direccion")


	def __str__(self):
		text = "{0} {1} {2} {3} {4} {5}"
		return text.format(self.persona, self.tiene_OS, self.obra_social, self.tipo_sangre, self.responsable, self.domicilio)

class Odontologo(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, related_name="pers2")
	especialidad = models.CharField(max_length= 255)

	def __str__(self):
		text = "{0} {1}"
		return text.format(self.persona, self.especialidad)

class Secretaria(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, related_name="pers3")

	def __str__(self):
		text = "{0}"
		return text.format(self.persona)

class Turno(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, related_name="paciente")
	odontologo = models.ForeignKey(Odontologo, on_delete=models.SET_NULL, null=True, related_name="odontologo")
	fecha = models.DateField() 
	hora = models.DateTimeField(auto_now = True) #verificar si es así
	motivo = models.CharField(max_length= 100)

	def __str__(self):
		text = "{0} {1} {2} {3} {4}"
		return text.format(self.paciente, self.odontologo, self.fecha, self.hora, self.motivo)


