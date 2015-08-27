#-*- coding: utf-8 -*-
"""
Clase PruebaAlumno para el problema 1 del Test de diseño para LemonTech.\n
"""

from Prueba import Prueba
from Alumno import Alumno

class PruebaAlumno(object):
    def __init__(self):
        self.prueba = Prueba()
        self.alumno = Alumno()
        self.nota = None

    @property
    def prueba(self):
        return self.__prueba

    @prueba.setter
    def prueba(self, prueba):
        self.__prueba = prueba

    @property
    def alumno(self):
        return self.__alumno

    @alumno.setter
    def alumno(self, alumno):
        self.__alumno = alumno

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota