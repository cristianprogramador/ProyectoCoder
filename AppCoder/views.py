from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario


# Create your views here.

#def curso(self):

    #curso = Curso(nombres='Backend', camada='12345')
    #curso.save()
    #documentoDeTexto = f'--->Curso: {curso.nombres} camada: {curso.camada}'
    #return HttpResponse(documentoDeTexto)

def inicio(request):
    #return HttpResponse('vista inicio')
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    if request.method == 'POST':

        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return redirect('inicio')
    else:
        mi_formulario = CursoFormulario()
    return render(request, 'AppCoder/cursos.html', {'cursos': mi_formulario})
    #return HttpResponse('vista curso')
    #return render(request, 'AppCoder/cursos.html')


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
    #return HttpResponse('vista estudiantes')
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    #return HttpResponse('vista entregable')
    return render(request, 'AppCoder/entregables.html')

def curso_formulario(request):
    if request.method == 'POST':

        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return redirect('inicio')
    else:
        mi_formulario = CursoFormulario()
    return render(request, 'AppCoder/curso-formulario.html', {'formulario_curso': mi_formulario})
