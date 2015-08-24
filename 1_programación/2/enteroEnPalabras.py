#-*- coding: utf-8 -*-
"""
Problema 1 del Test de programación para LemonTech.\n
<Escriba una función/método que dado un número entero, entregue su representación en palabras, Ej. 145 ­> "ciento cuarenta y cinco">
"""

from sys import argv, maxint
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
        """Método principal para convertir el entero en palabras.
            :param parametro: Número a convertir en palabras."""
        self.validarParametro(parametro)

        return self.convertirNumero(int(parametro))

    def convertirNumero(self, n):
        """Metodo recursivo para convertir el entero en palabras.
        :param n: Número a convertir en palabras."""
        # 10 ** 18?
        # Calculo de las billonesimas
        prim, resto = divmod(n, 1000000000)
        if prim != 0:
            if prim == 1:
                salida = "un " + OTROS[2]
            else:
                salida = self.convertirNumero(prim) + " " + OTROS[2] + "es"

            if resto != 0:
                salida = salida + " " + self.convertirNumero(resto)
        else:
            # Calculo de las millonesimas
            prim, resto = divmod(n, 1000000)
            if prim != 0:
                if prim == 1:
                    salida = "un " + OTROS[1]
                else:
                    salida = self.convertirNumero(prim) + " " + OTROS[1] + "es"

                if resto != 0:
                    salida = salida + " " + self.convertirNumero(resto)
            else:
                # Calculo de las milesimas
                prim, resto = divmod(n, 1000)
                if prim != 0:
                    if prim == 1:
                        salida = OTROS[0]
                    else:
                        salida = self.convertirNumero(prim) + " " + OTROS[0]

                    if resto != 0:
                        salida = salida + " " + self.convertirNumero(resto)

                else:
                    # Calculo de las centenas
                    prim, resto = divmod(n, 100)
                    if prim != 0:
                        if resto == 0 and prim == 1:
                            salida = CENTENAS[0]
                        else:
                            salida = CENTENAS[prim]

                        if resto != 0:
                            salida = salida + " " + self.convertirNumero(resto)
                    else:
                        # Calculo de las decenas
                        if resto <= 20:
                            salida = UNIDADES[n]
                        else:
                            prim, resto = divmod(n, 10)
                            salida = DECENAS[prim-2]
                            if resto != 0:
                                if prim == 2:
                                    salida = salida + UNIDADES[resto]
                                else:
                                    salida = salida + " y " + UNIDADES[resto]

        return salida

    def validarParametro(self, parametro):
        """Método para validar que el parámetro ingresado sea correcto.
            :param parametro: Parámetro a validar."""
        try:
            validar = int(parametro)
            if validar < 0:
                self.msjError("El parametro debe ser un entero positivo.")
            elif validar > maxint:
                self.msjError("El parametro excede el entero maximo para python2.\n\tsys.maxint = " + str(maxint))
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