from django.urls import path
from .views import *


urlpatterns = [
    path('',inicio),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),

]