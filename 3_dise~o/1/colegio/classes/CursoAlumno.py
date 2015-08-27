#-*- coding: utf-8 -*-
"""
Clase CursoAlumno para el problema 1 del Test de diseño para LemonTech.\n
"""

from Curso import Curso
from Alumno import Alumno

class CursoAlumno(object):
    def __init__(self):
        self.curso = Curso()
        self.alumno = Alumno()

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def alumno(self):
        return self.__alumno

    @alumno.setter
    def alumno(self, alumno):
        self.__alumno = alumno