from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from finalapp.models import Career
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
    career = Career.objects.all()
    return render(request, 'carreras.html', {
        'career': career,
        'titulo':'Carreras',
        'mensaje':'Listado de Carreras',
    })

def crear_carrera(request):
    return render(request, 'crear_carrera.html', {
        'titulo':'Agregar carreras',
        'mensaje':'Agregar Carrera',
    })

def eliminar_career(request, id):
    career = Career.objects.get(pk=id)
    career.delete()
    return redirect('carreras')

def save_career(request):
    
    if request.method == 'GET':
        name = request.GET['name']
        corto = request.GET['corto']
        image = request.GET['image']
        state = request.GET['state']
        
        career = Career(
            name = name,
            corto = corto,
            image=image,
            state=state
        )
        career.save()

        messages.success(request, f'Se agregó correctamente la carrera llamada: {career.name}')
        return redirect('carreras')

    else:
        return HttpResponse("<h2>No se ha podido registrar la carrera</h2>")
