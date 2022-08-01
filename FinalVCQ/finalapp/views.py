from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
# Create your views here.
from finalapp.models import Course 
from django.contrib import messages

layout = """"""
def cursos(request):
     cursos = Course.objects.all()
     return render(request, 'cursos.html', {
        'cursos':cursos,
        'titulo':'Cursos',
        'mensaje':'Listado de Cursos',
    })

def eliminar_curso(request, id):
    curso = Course.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

def save_curso(request):
    
    if request.method == 'GET':
        code = request.GET['code']
        name = request.GET['name']
        hour = request.GET['hour']
        credits = request.GET['credits']
        state = request.GET['state']
        
        curso = Course(
            code = code,
            name = name,
            hour = hour,
            credits=credits,
            state=state
        )
        curso.save()

        messages.success(request, f'Se agregó correctamente el curso llamado: {curso.name}')
        return redirect('cursos')

    else:
        return HttpResponse("<h2>No se ha podido registrar el curso</h2>")

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


