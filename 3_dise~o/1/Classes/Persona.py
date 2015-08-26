#-*- coding: utf-8 -*-
"""
Clase Persona para el problema 1 del Test de diseño para LemonTech.\n
"""

class Persona(object):
    def __init__(self):
        """Inicializador de la clase."""
        # Atributos de la clase
        self.xPers = None
        self.run = None
        self.nombre = None
        self.apellido = None
        self.apellido2 = None
        self.correoElectronico = None
        self.nacimiento = None
        self.activo = True

    @property
    def xPers(self):
        return self.__xPers

    @xPers.setter
    def xPers(self, xPers):
        self.__xPers = xPers

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, run):
        self.__run = run

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def apellido2(self):
        return self.__apellido2

    @apellido2.setter
    def apellido2(self, apellido2):
        self.__apellido2 = apellido2

    @property
    def correoElectronico(self):
        return self.__correoElectronico

    @correoElectronico.setter
    def correoElectronico(self, correoElectronico):
        self.__correoElectronico = correoElectronico

    @property
    def nacimiento(self):
        return self.__nacimiento

    @nacimiento.setter
    def nacimiento(self, nacimiento):
        self.__nacimiento = nacimiento

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, activo):
        self.__activo = activo

