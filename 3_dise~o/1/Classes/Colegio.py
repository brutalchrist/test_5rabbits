#-*- coding: utf-8 -*-
"""
Clase Colegio para el problema 1 del Test de diseño para LemonTech.\n
"""

class Colegio(object):
    def __init__(self):
        """Inicializador de la clase."""
        self.xCole = None
        self.rut = None
        self.nombre = None
        self.direccion = None

    @property
    def xCole(self):
        return self.__xCole

    @xCole.setter
    def xCole(self, xCole):
        self.__xCole = xCole

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, rut):
        self.__rut = rut

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion
