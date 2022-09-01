from django.db import models

#class Familiar(models.Model): 
    #nombre=models.CharField(max_length=40)
    #fecha_nacimiento=models.DateField()
    
class Familiar1(models.Model): 
    nombre=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    hijos=models.CharField(max_length=15)

class Amigo(models.Model):
    nombre=models.CharField(max_length=40)
    apodo=models.CharField(max_length=40)
    de_donde=models.CharField(max_length=40)

class Trabajos(models.Model):
    empresa=models.CharField(max_length=40)
    puesto=models.CharField(max_length=40)
    tarea=models.CharField(max_length=250)
    desde=models.DateField()
    hasta=models.DateField()


