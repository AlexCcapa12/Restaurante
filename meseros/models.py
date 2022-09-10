from django.db import models

class Meseros(models.Model):
    edad = models.CharField(max_length=20, default='')
    procedencia = models.CharField(max_length=20, default='')
