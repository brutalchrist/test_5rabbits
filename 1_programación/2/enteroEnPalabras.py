# -*- coding: utf-8 -*-

from sys import argv
from time import strftime
from constantes import *

USO = "\nUso:\n    python enteroEnpalabras.py X\n    X = entero positivo"

class EnteroEnPalabras():
    """Clase de pruebas"""
    def __init__(self):
        """Inicializador de la clase."""
        if len(argv) != 2:
            self.msjError("No coinciden los parametros." + USO)

    def enteroEnPalabras(self, parametro):
        self.validarParametro(parametro)

        #listaNumero = list(parametro)

        if int(parametro) <= 20:
            print self.unidadPalabra(int(parametro))
        elif int(parametro) <= 100:
            print self.decenaPalabra(int(parametro))
        elif int(parametro) <= 1000:
            print "cente"


    def unidadPalabra(self, n):
        return UNIDADES[n]

    def decenaPalabra(self, n):
        lista = list(str(n))

        if n < 30:
            return DECENAS[int(lista[0])-2] + UNIDADES[int(lista[1])]
        else:
            if n % 10 == 0:
                return DECENAS[int(lista[0])-2]
            else:
                return DECENAS[int(lista[0])-2] + ' y ' + UNIDADES[int(lista[1])]



    def validarParametro(self, parametro):
        """Método para validar que el parámetro ingresado sea correcto.
            :param parametro: Parámetro a validar."""
        try:
            validar = int(parametro)
            if validar < 0:
                self.msjError("El parametro debe ser un entero positivo.")
        except ValueError:
            self.msjError("El parametro debe ser un entero positivo.")


    def msjError(self, mensaje):
        """Método para desplegar un mensaje de error.
            :param mensaje: Mensaje de error."""
        print "[" + strftime("%H:%M:%S") + "] ERROR: " + mensaje
        exit(0)


if __name__ == '__main__':
    enteroEnPalabras = EnteroEnPalabras().enteroEnPalabras(argv[1])