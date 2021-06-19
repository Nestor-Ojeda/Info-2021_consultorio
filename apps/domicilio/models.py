from django.db import models

# Create your models here.

class Paises(models.Model):
		codigo = models.CharField(max_length = 2)
		pais = models.CharField(max_length=100)
		estado = models.BooleanField('Estado', default = True)

		def __str__(self):
			texto = '{0} {1} {2}'
			return texto.format(self.codigo, self.pais, self.estado)

class Provincia(models.Model):
	pais = models.ForeignKey(Paises, on_delete=models.SET_NULL, null=True)
	nombre = models.CharField(max_length=100)
	estado = models.BooleanField('Estado', default = True)

	def __str__(self):
			texto = '{0} {1} {2}'
			return texto.format(self.pais, self.nombre, self.estado)

class Ciudad(models.Model):
	provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
	cod_Postal = models.CharField(max_length=10)
	nom_ciudad = models.CharField(max_length=100)
	estado = models.BooleanField('Estado', default = True)

	def __str__(self):
			texto = '{0} {1} {2} {3}'
			return texto.format(self.provincia, self.nom_ciudad, self.cod_Postal, self.estado)

class Direccion(models.Model):
	ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
	barrio = models.CharField(max_length=100)
	calle = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	nota = models.TextField(max_length=300)
	estado = models.BooleanField('Estado', default = True)

	def __str__(self):
		tex = "{0} {1} {2} {3} {4} {5}"
		return tex.format(self.ciudad, self.barrio, 
			self.calle, self.numero, self.nota, self.estado)

