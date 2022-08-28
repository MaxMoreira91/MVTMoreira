from http.client import HTTPResponse
from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
import datetime

# Create your views here.

def padre(request):
    papa=Familia(nombre="Cesar Moreira", edad=62, nacimiento="1960-01-31")
    papa.save()
    mensaje=f"Familiar Moreira nombre:{papa.nombre} edad:{papa.edad} fecha de nacimiento {papa.nacimiento}"
    return HttpResponse(mensaje)

def madre(request):
    mama=Familia(nombre="Marta Maidana", edad=59, nacimiento="1963-10-25")
    mama.save()
    mensaje1=f"Familiar Moreira nombre:{mama.nombre} edad:{mama.edad} fecha de nacimiento {mama.nacimiento}"
    return HttpResponse(mensaje1)

def hermano(request):
    bro=Familia(nombre="Cesar Moreira", edad=30, nacimiento="1991-10-22")
    bro.save()
    mensaje2=f"Familiar Moreira nombre:{bro.nombre} edad:{bro.edad} fecha de nacimiento {bro.nacimiento}"
    return HttpResponse(mensaje2)
