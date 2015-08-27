#-*- coding: utf-8 -*-
"""
Clase Profesor para el problema 1 del Test de diseño para LemonTech.\n
"""

from Persona import Persona

class Profesor(Persona):
    def __init__(self):
        """Inicializador de la clase."""
        # Se extiende de Persona
        Persona.__init__(self)
        # Atributos de la clase
        self.sueldo = None
        self.titulo = None

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self.__sueldo = sueldo

