from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
# Create your views here.
layout = """"""
def cursos(request):
    return render(request, 'cursos.html', {
        'titulo':'Cursos',
        'mensaje':'Listado de Cursos',
    })

def crear_curso(request):
    return render(request, 'crear_curso.html', {
        'titulo':'Agregar curso',
        'mensaje':'Agregar Curso',
    })

def carreras(request):
    return render(request, 'carreras.html', {
        'titulo':'Carreras',
        'mensaje':'Listado de Carreras',
    })

def crear_carrera(request):
    return render(request, 'crear_carrera.html', {
        'titulo':'Agregar carreras',
        'mensaje':'Agregar Carrera',
    })
