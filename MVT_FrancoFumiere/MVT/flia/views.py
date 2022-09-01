from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar1, Amigo, Trabajos
from django.template import loader

def inicio(reuqest):
    return render (request, "flia/inicio.html")

def familia(reuqest):
    return render (request, "flia/familia.html")

def amigos(reuqest):
    return render (request, "flia/amigos.html")

def trabajo(reuqest):
    return render (request, "flia/trabajos.html")




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

    Fede=Familiar1(nombre="Federico", fecha_nacimiento="1987-04-01", hijos="0")
    Fede.save()
    texto=f"Mi nombre es {Fede.nombre} y nací en {Fede.fecha_nacimiento}. A día de hoy, tengo {Fede.hijos} hijo"
    
    return HttpResponse(texto)

def Thomy(request):

    Thomy=Amigo (nombre='Thomy',apodo='karate', de_donde='Colegio San Ana')
    Thomy.save()
    texto=f'Mi nombre es {Thomy.nombre}, me dicen {Thomy.apodo} y lo conozco a Franco de {Thomy.de_donde}.'
    return HttpResponse(texto)


    #plantilla=loader.get_template('template.html')
    #diccionario={nombre='nombre', apellido='apellido'}
    #documento=plantilla.render(diccionario)
    #return HttpResponse(texto)  
    #NO ESTÁ IMPORTADO EL LOADER NI EL TEMPLATE A PROPOSITO EN ESTE VIEWS 