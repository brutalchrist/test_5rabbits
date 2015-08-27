#-*- coding: utf-8 -*-
"""
Clase Alumno para el problema 1 del Test de diseño para LemonTech.\n
"""

from Persona import Persona

class Alumno(Persona):
    def __init__(self):
        """Inicializador de la clase."""
        # Se extiende de Persona
        Persona.__init__()
        # Atributos de la clase
        self.becado = False

    @property
    def becado(self):
        return self.__becado

    @becado.setter
    def becado(self, becado):
        self.__becado = becado
