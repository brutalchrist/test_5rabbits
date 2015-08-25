#-*- coding: utf-8 -*-
"""
Problema 3 del Test de programación para LemonTech.\n
<Considere un tablero de ajedrez de NxN, realice un algoritmo que visite cada espacio del tablero, usando solamente los movimientos de un caballo. (Puntos extras si se visita cada espacio una sola vez)>
"""

from sys import argv, platform
from time import strftime, sleep
from os import system
from Caballo import *

# Defines
USO = "\nUso:\n    python tablero.py X\n    X > 4"
LINUX = "linux2"
WINDOWS = "win32"
MACOS = "darwin"
DELAY = 0.2

class Tablero():
    """Clase de prueba"""
    def __init__(self):
        """Inicializador de la clase."""
        if len(argv) > 2:
            self.msjError("No coinciden los parametros." + USO)

        self.terminado = False
        self.caballo = Caballo()

    def movimientoDelCaballo(self, parametro="DEFAULT"):
        if parametro != "DEFAULT":
            self.validarParametro(parametro)

        if parametro != "DEFAULT":
            self.rangoTablero = int(parametro)
        else:
            self.rangoTablero = self.caballo.getTablero()

        self.tablero = [["   " for i in xrange(self.rangoTablero)] for i in xrange(self.rangoTablero)]

        self.caballo.setTablero(self.rangoTablero)
        self.dibujarCaballo()
        self.dibujarTablero()
        self.jugar(0)

        print "No hay solución"

    def jugar(self, contador):
        contador = contador + 1
        pos = self.caballo.getXY()

        movimientosPosibles = self.movimientosPosibles()
        movimientosPosibles = self.menosProbable(movimientosPosibles)

        for movimiento in movimientosPosibles:
            pos_ant = pos
            self.dibujarContador(contador)
            self.moverCaballo(movimiento)
            self.dibujarTablero()
            if self.tableroLleno():
                print "Completado!"
                exit(0)
            pos = self.caballo.getXY()
            self.jugar(contador)
            self.moverCaballoBorrar(pos, pos_ant)
            pos = self.caballo.getXY()
            self.dibujarTablero()

    def menosProbable(self, posPosibles):
        listaPosibles = []
        for movimiento in posPosibles:
            movActual = self.caballo.getXY()
            self.moverCaballo(movimiento)
            posibles = len(self.movimientosPosibles())
            x, y = movimiento[1]
            self.moverCaballoBorrar((int(x), int(y)), movActual)
            listaPosibles.append(posibles)
        return self.ordenar(listaPosibles, posPosibles)

    def ordenar(self, listaNumPosibles, listaOrdenar):
        for i in range(len(listaNumPosibles)):
            for j in range(len(listaNumPosibles) -1):
                if listaNumPosibles[j] > listaNumPosibles[j+1]:
                    listaOrdenar[j], listaOrdenar[j+1] = listaOrdenar[j+1], listaOrdenar[j]
                    listaNumPosibles[j], listaNumPosibles[j+1] = listaNumPosibles[j+1], listaNumPosibles[j]

        return listaOrdenar

    def movimientosPosibles(self):
        movimentosCaballo = self.caballo.movimientosPosibles(self.rangoTablero)
        movimientos = []
        for mov in movimentosCaballo:
            x, y = mov[1]
            if self.tablero[x][y] == "   ":
                movimientos.append(mov)
        return movimientos

    def moverCaballo(self, movimiento):
        if movimiento[0] == "SDL":
            self.caballo.movSupDerLar(True)
        if movimiento[0] == "SIL":
            self.caballo.movSupIzqLar(True)
        if movimiento[0] == "SDC":
            self.caballo.movSupDerCor(True)
        if movimiento[0] == "SIC":
            self.caballo.movSupIzqCor(True)
        if movimiento[0] == "IDL":
            self.caballo.movInfDerLar(True)
        if movimiento[0] == "IIL":
            self.caballo.movInfIzqLar(True)
        if movimiento[0] == "IDC":
            self.caballo.movInfDerCor(True)
        if movimiento[0] == "IIC":
            self.caballo.movInfIzqCor(True)

        self.dibujarCaballo()

    def moverCaballoBorrar(self, pos, posAnterior):
        self.tablero[pos[0]][pos[1]] = "   "
        self.caballo.setXY(posAnterior[0], posAnterior[1])
        self.dibujarCaballo()

    def dibujarCaballo(self):
        self.tablero[self.caballo.getX()][self.caballo.getY()] = '°M~'  # Si, es un caballo.

    def dibujarContador(self, contador):
        if(contador < 10):
            self.tablero[self.caballo.getX()][self.caballo.getY()] = '  ' + str(contador)
        elif(contador < 100):
            self.tablero[self.caballo.getX()][self.caballo.getY()] = ' ' + str(contador)
        else:
            self.tablero[self.caballo.getX()][self.caballo.getY()] = str(contador)


    def tableroLleno(self):
        for y in range(self.rangoTablero):
            for x in range(self.rangoTablero):
                if self.tablero[x][y] == "   ":
                    return False
        return True

    def dibujarTablero(self):
        self.limpiarPantalla()
        print "\n"
        for y in range(self.rangoTablero):
            fila = "\t| "
            for x in range(self.rangoTablero):
                fila = fila + str(self.tablero[x][y]) + " | "
            print fila
        print
        sleep(DELAY)

    def limpiarPantalla(self):
        if platform == LINUX or platform == MACOS:
           system('clear')
        elif platform == WINDOWS:
            system('cls')

    def validarParametro(self, parametro):
        """Método para validar que el parámetro ingresado sea correcto.
            :param parametro: Parámetro a validar."""
        try:
            validar = int(parametro)
            if validar < 0:
                self.msjError("El parametro debe ser un entero positivo.")
            elif validar < 5:
                self.msjError("El tamaño mínimo del tablero debe ser 5x5.")
        except ValueError:
            self.msjError("El parametro debe ser un entero positivo.")

    def msjError(self, mensaje):
        """Método para desplegar un mensaje de error.
            :param mensaje: Mensaje de error."""
        print "[" + strftime("%H:%M:%S") + "] ERROR: " + mensaje
        exit(0)


if __name__ == '__main__':
    tablero = Tablero()
    if len(argv) == 2:
        tablero.movimientoDelCaballo(argv[1])
    elif len(argv) == 1:
        tablero.movimientoDelCaballo()
