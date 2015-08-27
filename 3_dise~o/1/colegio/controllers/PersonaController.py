#-*- coding: utf-8 -*-
"""
Clase PersonaController para el problema 1 del Test de diseño para LemonTech.\n
"""
from sys import path

path.append('../classes')
from Persona import Persona

class PersonaController(object):
    def __init__(self):
        self.persona = Persona()

    def busqueda(self, xPers):
        """Busca una persona por su Clave primaria.
            :parameter:
                - xPers: Clave primaria de la persona"""

    def busquedaPorRun(self, run):
        """Busca una persona por su RUN.
            :parameter:
                - run: Run de la persona"""

    def activarPersona(self, persona):
        """Activa una persona.
            :parameter:
                - xPers: Clave primaria"""

    def eliminarPersona(self, persona):
        """Elimina a una Persona.
            :parameter:
                - persona: Persona a eliminar."""

    def actualizaPersona(self, persona):
        """Actualiza a una Persona.
            :parameter:
                - persona: Persona a actualizar."""

    def agregarPersona(self, persona):
        """Agrega a una Persona.
            :parameter:
                - persona: Persona a agregar."""



