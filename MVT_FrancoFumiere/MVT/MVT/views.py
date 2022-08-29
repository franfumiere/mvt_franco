from django.shortcuts import render
from django.http import HttpResponse
#from .models import Familiar1
from django.template import Template, loader

def probando(request):
    nombre=('Silvana')
    apellido=('Becce')

    plantilla=loader.get_template('template.html')
    diccionario={nombre:'nombre', apellido:'apellido'}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)