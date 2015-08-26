#-*- coding: utf-8 -*-
"""
Clase Prueba para el problema 1 del Test de diseño para LemonTech.\n
"""

from Curso import Curso

class Prueba(object):
    def __init__(self):
        self.xPrue = None
        self.curso = Curso()
        self.nombre = None
        self.rendicion = None
        self.duracion = None

    @property
    def xPrue(self):
        return self.__xPrue

    @xPrue.setter
    def xPrue(self, xPrue):
        self.__xPrue = xPrue

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def rendicion(self):
        return self.__rendicion

    @rendicion.setter
    def rendicion(self, rendicion):
        self.__rendicion = rendicion

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion