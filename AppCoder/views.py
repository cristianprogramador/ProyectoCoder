from django.shortcuts import render
from django.http import HttpResponse
#from AppCoder.models import Curso


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
    #return HttpResponse('vista curso')
    return render(request, 'AppCoder/cursos.html')


def profesores(request):
    #return HttpResponse('vista profesores')
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    #return HttpResponse('vista estudiantes')
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    #return HttpResponse('vista entregable')
    return render(request, 'AppCoder/entregables.html')


