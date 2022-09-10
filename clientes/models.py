from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=20)



