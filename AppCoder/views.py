from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso


# Create your views here.

#def curso(self):

    #curso = Curso(nombres='Backend', camada='12345')
    #curso.save()
    #documentoDeTexto = f'--->Curso: {curso.nombres} camada: {curso.camada}'
    #return HttpResponse(documentoDeTexto)

def inicio(request):
    return HttpResponse('vista inicio')

def curso(request):
    return HttpResponse('vista curso')

def profesores(request):
    return HttpResponse('vista profesores')

def estudiantes(request):
    return HttpResponse('vista estudiantes')

def entregables(request):
    return HttpResponse('vista entregable')
    

