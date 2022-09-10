from django.db import models

class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.CharField(max_length=20)
    procedencia = models.CharField(max_length=20, default='')


    #def __str__(self):
        #return "{} tiene {} años" .format(self.nombre, self.edad)
