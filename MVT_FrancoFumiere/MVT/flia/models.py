from django.db import models

class Familiar(models.Model): 
    nombre=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    
class Familiar1(models.Model): 
    nombre=models.CharField(max_length=40)
    fecha_nacimiento=models.DateField()
    hijos=models.CharField(max_length=15)
