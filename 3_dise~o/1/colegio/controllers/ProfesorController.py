#-*- coding: utf-8 -*-
"""
Clase ProfesorController para el problema 1 del Test de diseño para LemonTech.\n
"""
from sys import path

path.append('../classes')
from Persona import Persona
from Curso import Curso

class ProfesorController():
    def __init__(self):
        self.persona = Persona()
        self.curso = Curso()

    def asignaPersonaComoProfesor(self, persona):
        """Asigna a una persona como Profesor.
            :parameter:
                - persona: Persona a asignar."""

    def buscarProfesorCurso(self, curso):
        """Busca un Profesor por su Curso.
            :parameter:
                - curso: Curso a buscar."""

    def busqueda(self, xPers):
        """Busca un Profesor por su Clave primaria.
            :parameter:
                - xPers: Clave primaria del Profesor."""

    def busquedaPorRun(self, run):
        """Busca un Profesor por su RUN.
            :parameter:
                - run: Run del Profesor."""

    def eliminarProfesor(self, profesor):
        """Elimina a un Profesor.
            :parameter:
                - profesor: Profesor a eliminar."""

    def actualizaPersona(self, profesor):
        """Actualiza a un Profesor.
            :parameter:
                - persona: Profesor a actualizar."""

    def agregarPersona(self, profesor):
        """Agrega a un Profesor.
            :parameter:
                - persona: Profesor a agregar."""
