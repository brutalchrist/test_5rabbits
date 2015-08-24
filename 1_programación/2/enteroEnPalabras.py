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
            return self.unidadPalabra(int(parametro))
        elif int(parametro) <= 100:
            return self.decenaPalabra(int(parametro))
        elif int(parametro) < 1000:
            return self.centenaPalabra(int(parametro))
        elif int(parametro) < 1000000:
            return self.milesimaPalabra(int(parametro))


    def unidadPalabra(self, n):
        return UNIDADES[n]

    def decenaPalabra(self, n):
        lista = list(str(n))

        if n <= 20:
            return self.unidadPalabra(n)
        elif n < 30:
            return DECENAS[int(lista[0])-2] + UNIDADES[int(lista[1])]
        else:
            if n % 10 == 0:
                return DECENAS[int(lista[0])-2]
            else:
                return DECENAS[int(lista[0])-2] + ' y ' + UNIDADES[int(lista[1])]

    def centenaPalabra(self, n):
        lista = list(str(n))

        return CENTENAS[int(lista[0])-1] + " " + self.decenaPalabra(int(lista[1] + lista[2]))

    def milesimaPalabra(self, n):
        lista = list(str(n))

        print len(lista)

        if len(lista) == 4:
            #todo: terminar
            if n < 2000:
                print int(lista[1] + lista[2] + lista[3])
                return OTROS[0] + " " + self.centenaPalabra(int(lista[1] + lista[2] + lista[3]))
            else:
                return self.unidadPalabra(int(lista[0])) + " " + OTROS[0] + " " + self.centenaPalabra(int(lista[1] + lista[2] + lista[3]))
        if len(lista) == 5:
            print "holi"
        if len(lista) == 6:
            print "holi"

        return "miles"



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
    print argv[1] + ": " + enteroEnPalabras