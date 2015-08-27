#-*- coding: utf-8 -*-
"""
Clase AlumnoController para el problema 1 del Test de diseño para LemonTech.\n
"""
from sys import path

path.append('../classes')
from Persona import Persona
from Alumno import Alumno
from Prueba import Prueba
from Curso import Curso

class AlumnoController():
    def __init__(self):
        self.persona = Persona()
        self.alumno = Alumno()
        self.prueba = Prueba()
        self.curso = Curso()

    def asignaPersonaComoAlumno(self, persona):
        """Asigna a una persona como Alumno.
            :parameter:
                - persona: Persona a asignar."""

    def becarAlumno(self, alumno):
        """Beca a un alumno.
            :parameter:
                - alumno: Alumno a becar."""

    def pruebasAlumno(self, alumno):
        """Busca las pruebas por Alumno.
            :parameter:
                - alumno: Alumno a buscar."""

    def buscarAlumnosPrueba(self, prueba):
        """Busca Alumno(s) que rindio(eron) una Prueba.
            :parameter:
                - prueba: Prueba a buscar."""

    def buscarAlumnosCurso(self, curso):
        """Busca Alumnos de un Curso.
            :parameter:
                - curso: Curso a buscar."""

    def busqueda(self, xPers):
        """Busca un Alumno por su Clave primaria.
            :parameter:
                - xPers: Clave primaria del Alumno."""

    def busquedaPorRun(self, run):
        """Busca un Alumno por su RUN.
            :parameter:
                - run: Run del Alumno."""

    def eliminarAlumno(self, alumno):
        """Elimina a un Alumno.
            :parameter:
                - alumno: Alumno a eliminar."""

    def actualizaAlumno(self, alumno):
        """Actualiza a un Alumno.
            :parameter:
                - alumno: Alumno a actualizar."""

    def agregarAlumno(self, alumno):
        """Agrega a un Alumno.
            :parameter:
                - alumno: Alumno a agregar."""