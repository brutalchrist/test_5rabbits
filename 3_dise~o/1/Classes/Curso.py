#-*- coding: utf-8 -*-
"""
Clase Curso para el problema 1 del Test de diseño para LemonTech.\n
"""

from Colegio import Colegio
from Profesor import Profesor

class Curso(object):
    def __init__(self):
        """Inicializador de la clase."""
        # Atributos de la clase
        self.xCurs = None
        self.colegio = Colegio()
        self.profesor = Profesor()
        self.nombre = None
        self.descripcion = None
        self.activo = True

    @property
    def xCurs(self):
        return self.__xCurs

    @xCurs.setter
    def xCurs(self, xCurs):
        self.__xCurs = xCurs

    @property
    def colegio(self):
        return self.__colegio

    @colegio.setter
    def colegio(self, colegio):
        self.__colegio = colegio

    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, activo):
        self.__activo = activo
