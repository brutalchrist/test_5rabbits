#-*- coding: utf-8 -*-
"""
Problema 3 del Test de programación para LemonTech.\n
<Considere un tablero de ajedrez de NxN, realice un algoritmo que visite cada espacio del tablero, usando solamente los movimientos de un caballo. (Puntos extras si se visita cada espacio una sola vez)>
"""

class Caballo():
    def __init__(self):
        self.x = 2
        self.y = 2
        self.tablero = 5

    def movSupDerLar(self, realizaMov=False):
        if (self.x + 1) > (self.tablero - 1) or (self.y - 2) < 0:
            return False
        if realizaMov:
            self.x = self.x + 1
            self.y = self.y - 2
            return self.x, self.y
        return self.x + 1, self.y - 2

    def movSupIzqLar(self, realizaMov=False):
        if (self.x - 1) < 0 or (self.y - 2) < 0:
            return False
        if realizaMov:
            self.x = self.x - 1
            self.y = self.y - 2
            return self.x, self.y
        return self.x - 1, self.y - 2

    def movSupDerCor(self, realizaMov=False):
        if (self.x + 2) > (self.tablero - 1) or (self.y - 1) < 0:
            return False
        if realizaMov:
            self.x = self.x + 2
            self.y = self.y - 1
            return self.x, self.y
        return self.x + 2, self.y - 1

    def movSupIzqCor(self, realizaMov=False):
        if (self.x - 2) < 0 or (self.y - 1) < 0:
            return False
        if realizaMov:
            self.x = self.x - 2
            self.y = self.y - 1
            return self.x, self.y
        return self.x - 2, self.y - 1

    def movInfDerLar(self, realizaMov=False):
        if (self.x + 1) > (self.tablero - 1) or (self.y + 2) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x + 1
            self.y = self.y + 2
            return self.x, self.y
        return self.x + 1, self.y + 2

    def movInfIzqLar(self, realizaMov=False):
        if (self.x - 1) < 0 or (self.y + 2) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x - 1
            self.y = self.y + 2
            return self.x, self.y
        return self.x - 1, self.y + 2

    def movInfDerCor(self, realizaMov=False):
        if (self.x + 2) > (self.tablero - 1) or (self.y + 1) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x + 2
            self.y = self.y + 1
            return self.x, self.y
        return self.x + 2, self.y + 1

    def movInfIzqCor(self, realizaMov=False):
        if (self.x - 2) < 0 or (self.y + 1) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x - 2
            self.y = self.y + 1
            return self.x, self.y
        return self.x - 2, self.y + 1

    def movimientosPosibles(self, n):
        listaMov = []

        if self.movSupDerLar():
            listaMov.append(["SDL", self.movSupDerLar()])
        if self.movSupIzqLar():
            listaMov.append(["SIL", self.movSupIzqLar()])
        if self.movSupDerCor():
            listaMov.append(["SDC", self.movSupDerCor()])
        if self.movSupIzqCor():
            listaMov.append(["SIC", self.movSupIzqCor()])
        if self.movInfDerLar():
            listaMov.append(["IDL", self.movInfDerLar()])
        if self.movInfIzqLar():
            listaMov.append(["IIL", self.movInfIzqLar()])
        if self.movInfDerCor():
            listaMov.append(["IDC", self.movInfDerCor()])
        if self.movInfIzqCor():
            listaMov.append(["IIC", self.movInfIzqCor()])

        return listaMov

    def setX(self, x):
        self.x = x

    def getX(self):
        return int(self.x)

    def setY(self, y):
        self.y = y

    def getY(self):
        return int(self.y)

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def getXY(self):
        return int(self.x), int(self.y)

    def setTablero(self, n):
        self.tablero = n

    def getTablero(self):
        return int(self.tablero)