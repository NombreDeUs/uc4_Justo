from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def listar_cursos(request):
    cursos = Course.objects.all()
    return render(request, 'listado_cursos.html', {'cursos': cursos})

def eliminar_curso(request, curso_id):
   curso = Course.objects.get(pk=curso_id)
   curso.delete()
   messages.success(request, 'Curso eliminado exitosamente.')
   return redirect('listado_cursos')

def crear_curso(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        hour = request.POST['hour']
        credits = request.POST['credits']
        state = request.POST['state']
        Course.objects.create(code=code, name=name, hour=hour, credits=credits, state=state)
        messages.success(request, 'Curso creado exitosamente.')
        return redirect('listado_cursos')
    return render(request, 'agregar_curso.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def cargar_cursos_untels(request):
    Course.objects.create(code='CURSO1', name='estadistica', hour=60, credits=4, state='Activo')
    Course.objects.create(code='CURSO2', name='lenguaje de programacion', hour=45, credits=3, state='Activo')
    Course.objects.create(code='CURSO3', name='microprocesadores', hour=90, credits=6, state='Inactivo')
    Course.objects.create(code='CURSO4', name='legislacion informatica', hour=30, credits=2, state='Activo')
    Course.objects.create(code='CURSO5', name='dinamica de sistemas', hour=75, credits=5, state='Inactivo')
    messages.success(request, 'Cursos de la UNTELS agregados exitosamente.')
    return redirect('listado_cursos')

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


