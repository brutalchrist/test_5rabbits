#-*- coding: utf-8 -*-
"""
Clase PruebaAlumnoController para el problema 1 del Test de diseño para LemonTech.\n
"""

from sys import path

path.append('../classes')
from Alumno import Alumno
from Prueba import Prueba

class CursoController():
    def __init__(self):
        self.alumno = Alumno()
        self.prueba = Prueba()

    def notaPruebaAlumno(self, prueba, alumno):
        """Busca nota de un Alumno en una Prueba.
            :parameter:
                - prueba: Prueba a buscar.
                - alumno: Alumno a buscar."""

    def notasPrueba(self, prueba):
        """Busca notas de una Prueba.
            :parameter:
                - prueba: Prueba a buscar."""

    def pruebasNota(self, prueba, nota):
        """Busca Pruebas con una determinada nota.
            :parameter:
                - prueba: Prueba a buscar.
                - nota: Nota a buscar."""


