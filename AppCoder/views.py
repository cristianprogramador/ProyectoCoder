from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario


# Create your views here.

# VISTAS DE PAGINAS NAVEGACION

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains = camada)
        return render(request, 'AppCoder/inicio.html', {'cursos': cursos, 'camada': camada})

    else: 
        respuesta = 'ERROR CAMPO SIN RELLENO'

    return render(request, 'AppCoder/inicio.html', {"respuesta": respuesta})

def cursos(request):
    mis_cursos = Curso.objects.all()

    if request.method == 'POST':
        # Aqui recibiremos toda las informacion enviada mediante el formulario
        mi_formulario = CursoFormulario(request.POST)
        # Validaremos que los datos correspondan con los esperados
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            nuevo_curso = {'nombre': informacion['curso'], 'camada': informacion['camada']}
            return render(request, 'AppCoder/cursos.html', {'cursos': mi_formulario, 'nuevo_curso': nuevo_curso, 'mis_cursos': mis_cursos})
    else:
        # inicializamos un formulario vacio para construir el HTML
        mi_formulario = CursoFormulario()
    # Mostramos la vista del formulario pero pensando el formulario vacio como contexto
    return render(request, 'AppCoder/cursos.html', {'cursos': mi_formulario, 'mis_cursos': mis_cursos})

def profesores(request):
    if request.method == 'POST':

        mi_formulario = ProfesorFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return redirect('inicio')
    else:
        mi_formulario = ProfesorFormulario()
    return render(request, 'AppCoder/profesores.html', {'profesores': mi_formulario})
    #return HttpResponse('vista profesores')
    #return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    if request.method == 'POST':

        mi_formulario = EstudianteFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return redirect('inicio')
    else:
        mi_formulario = EstudianteFormulario()
    return render(request, 'AppCoder/estudiantes.html', {'estudiante': mi_formulario})
    #return HttpResponse('vista estudiantes')
    #return render(request, 'AppCoder/estudiantes.html')


    if request.method == 'POST':

        mi_formulario = EntregableFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            entregable = Entregable(nombre=informacion['nombre'], fecha_de_entrega=informacion['fechadeentrega'], entregado=informacion['entregado'])
            entregable.save()
            return redirect('inicio')
    else:
        mi_formulario = EntregableFormulario()
    return render(request, 'AppCoder/entregables.html', {'entregables': mi_formulario})
    #return HttpResponse('vista entregable')
    #return render(request, 'AppCoder/entregables.html')