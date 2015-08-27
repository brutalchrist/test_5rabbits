#-*- coding: utf-8 -*-
"""
Clase PruebaController para el problema 1 del Test de diseño para LemonTech.\n
"""
from sys import path

path.append('../classes')
from Alumno import Alumno
from Prueba import Prueba

class PruebaController():
    def __init__(self):
        self.alumno = Alumno()
        self.prueba = Prueba()

    def buscarCursoPrueba(self, prueba):
        """Busca el Curso de una Prueba.
            :parameter:
                - prueba: Prueba a buscar."""

    def buscarProfesorPrueba(self, prueba):
        """Busca el Profesor que tomó una Prueba.
            :parameter:
                - prueba: Prueba a buscar."""

    def buscarPruebasProfesor(self, profesor):
        """Busca las pruebas que tomó un Profesor.
            :parameter:
                - prueba: Prueba a buscar."""

    def busqueda(self, xPrue):
        """Busca una Prueba por su Clave primaria.
            :parameter:
                - xPrue: Clave primaria de la Prueba."""

    def busquedaFecha(self, fecha):
        """Busca una Prueba su fecha.
            :parameter:
                - fecha: Fecha a buscar una(s) Prueba(s)."""

    def eliminarPrueba(self, prueba):
        """Elimina una Prueba.
            :parameter:
                - prueba: Prueba a eliminar."""

    def actualizaPrueba(self, prueba):
        """Actualiza una Prueba.
            :parameter:
                - prueba: Prueba a actualizar."""

    def agregarPrueba(self, prueba):
        """Agrega una Prueba.
            :parameter:
                - prueba: Prueba a agregar."""