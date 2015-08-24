# -*- coding: utf-8 -*-

from sys import argv
from time import strftime
from math import factorial

# Defines
MATH = False    # Define si el calculo del factoríal se realiza de manera manual o utilizando la librería math
USO = "\nUso:\n    python cerosDerechaFactorial.py X\n    X = entero positivo"

class CerosDerechaFactorial():
    """Clase de prueba"""
    def __init__(self):
        """Inicializador de la clase."""
        if len(argv) != 2:
            self.msjError("No coinciden los parametros." + USO)


    def cerosDerechaFactorial(self, parametro):
        """Método principal para calcular los ceros a la derecha de n factorial.
            :param parametro: Número a calcular su factorial y los ceros a la derecha del mismo"""
        self.validarParametro(parametro)

        if MATH:
            factorial = self.calcularFactorialMath(parametro)
        else:
            factorial = self.calcularFactorial(parametro)

        return self.calcularCerosDerecha(factorial)


    def calcularFactorial(self, n):
        """Método para calcular el factorial de un número de manera manual.
            :param n: Número a calcular su factorial."""
        resultado = 1
        n_int = int(n)

        while n_int >= 1:
            resultado = resultado * n_int
            n_int = n_int - 1

        return resultado


    def calcularFactorialMath(self, n):
        """Método para calcular el factorial de un número utilizando la librería Math.
            :param n: Número a calcular su factorial."""
        return factorial(int(n))

    def calcularCerosDerecha(self, n):
        """Método para calcular los ceros a la derecha de un numero.
            :param n: Número a calcular sus ceros a la derecha."""
        cerosDerecha = 0
        while True:
            """El cálculo del modulo y de n también se puede realiza utilizando la función divmod:
                n, modulo = divmod(n, 10)"""
            modulo = n % 10
            n = n // 10

            if modulo != 0: break

            cerosDerecha = cerosDerecha + 1

        return cerosDerecha


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
    cerosDerecha = CerosDerechaFactorial().cerosDerechaFactorial(argv[1])

    print "Los ceros a la derecha de " + str(argv[1]) + "! son " +  str(cerosDerecha)

