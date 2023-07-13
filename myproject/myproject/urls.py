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
    path('crear_curso/', views.agregar_curso, name='agregar_curso'),
    path('carreras/', views.listado_carreras, name='listado_carreras'),
    path('crear_carrera/', views.agregar_carrera, name='agregar_carrera'),
]

