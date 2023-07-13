"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from nombre_app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.listado_cursos, name='listado_cursos'),
    path('cursos/crear/', views.crear_curso, name='agregar_curso'),
   
    
    path('cursos/', views.listar_cursos, name='listado_cursos'),
    path('cursos/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('carreras/', views.listar_carreras, name='listado_carreras'),
    path('carreras/eliminar/<int:carrera_id>/', views.eliminar_carrera, name='eliminar_carrera'),
    path('crear_carrera/', views.crear_carrera, name='crear_carrera'),
    path('crear_carrera/', views.agregar_carrera, name='agregar_carrera'),
     path('carreras/', views.listado_carreras, name='listado_carreras'),
]

