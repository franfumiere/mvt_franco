from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar1


def Silvana(request):
    Silvana= Familiar1(nombre="Silvana", fecha_nacimiento="1979-02-28", hijos="1")
    Silvana.save()
    texto=f"Mi nombre es {Silvana.nombre} y nací en {Silvana.fecha_nacimiento}. A día de hoy, tengo {Silvana.hijos} hijo"
    return HttpResponse (texto)

def Lola(request):
    Lola=Familiar1(nombre="Lola", fecha_nacimiento="2002-08-06", hijos="0")
    Lola.save()
    texto=f"Mi nombre es {Lola.nombre} y nací en {Lola.fecha_nacimiento}. A día de hoy, tengo {Lola.hijos} hijo"
    return HttpResponse(texto)

def Fede(request):
    Fede=Familiar1(nombre="Federico", fecha_nacimiento="1987-04.01", hijos="0")
    Fede.save()
    texto=f"Mi nombre es {Fede.nombre} y nací en {Fede.fecha_nacimiento}. A día de hoy, tengo {Fede.hijos} hijo"
    return HttpResponse(texto)