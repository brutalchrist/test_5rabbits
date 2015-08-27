#-*- coding: utf-8 -*-
"""
Clase CursoController para el problema 1 del Test de diseño para LemonTech.\n
"""
from sys import path

path.append('../classes')
from Alumno import Alumno
from Prueba import Prueba
from Colegio import Colegio

class CursoController():
    def __init__(self):
        self.alumno = Alumno()
        self.prueba = Prueba()
        self.colegio = Colegio()

    def buscarCursosColegio(self, colegio):
        """Busca Cursos de un Colegio.
            :parameter:
                - colegio: Colegio a buscar."""

    def buscarCursosProfesor(self, profesor):
        """Busca Cursos de un Profesor.
            :parameter:
                - profesor: Profesor a buscar."""

    def busqueda(self, xCurs):
        """Busca una Curso por su Clave primaria.
            :parameter:
                - xCurs: Clave primaria de la Curso."""

    def eliminarCurso(self, curso):
        """Elimina un Curso.
            :parameter:
                - curso: Curso a eliminar."""

    def actualizaCurso(self, curso):
        """Actualiza un Curso.
            :parameter:
                - curso: Curso a actualizar."""

    def agregarCurso(self, curso):
        """Agrega a un Curso.
            :parameter:
                - curso: Curso a agregar."""
