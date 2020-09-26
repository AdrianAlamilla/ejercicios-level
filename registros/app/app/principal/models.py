from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200)
    kilometros = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

