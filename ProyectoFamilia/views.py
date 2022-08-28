from django.template import Template, Context
from django.http import HttpResponse


def familiaMoreira(request):
    miArchivo=open("C:/Users/Usuario/Desktop/primeros pasos/Familia/ProyectoFamilia/plantilla/temple1.html")
    contenido=miArchivo.read()
    miArchivo.close()
    plantilla=Template(contenido)
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse(documento)