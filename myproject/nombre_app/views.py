from django.shortcuts import render
from django.http import HttpResponse

def listado_cursos(request):
    return HttpResponse("Listado de Cursos")

def agregar_curso(request):
    return HttpResponse("Agregar Curso")

def listado_carreras(request):
    return HttpResponse("Listado de Carreras")

def agregar_carrera(request):
    return HttpResponse("Agregar Carreras")

def inicio(request):
    return render(request, 'inicio.html')
