#-*- coding: utf-8 -*-
"""
Clase externa para el problema 3 del Test de programación para LemonTech.\n
<Considere un tablero de ajedrez de NxN, realice un algoritmo que visite cada espacio del tablero, usando solamente los movimientos de un caballo. (Puntos extras si se visita cada espacio una sola vez)>
"""

class Caballo():
    """Clase Caballo."""
    def __init__(self):
        """Inicializador de la clase."""
        self.x = 2  # Valores por defecto
        self.y = 2
        self.tablero = 5

    def movSupDerLar(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición superior derecha más alta.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x + 1) > (self.tablero - 1) or (self.y - 2) < 0:
            return False
        if realizaMov:
            self.x = self.x + 1
            self.y = self.y - 2
            return self.x, self.y
        return self.x + 1, self.y - 2

    def movSupIzqLar(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición superior izquierda más alta.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x - 1) < 0 or (self.y - 2) < 0:
            return False
        if realizaMov:
            self.x = self.x - 1
            self.y = self.y - 2
            return self.x, self.y
        return self.x - 1, self.y - 2

    def movSupDerCor(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición superior derecha menos alto.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x + 2) > (self.tablero - 1) or (self.y - 1) < 0:
            return False
        if realizaMov:
            self.x = self.x + 2
            self.y = self.y - 1
            return self.x, self.y
        return self.x + 2, self.y - 1

    def movSupIzqCor(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición superior izquiero menos alto.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x - 2) < 0 or (self.y - 1) < 0:
            return False
        if realizaMov:
            self.x = self.x - 2
            self.y = self.y - 1
            return self.x, self.y
        return self.x - 2, self.y - 1

    def movInfDerLar(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición inferior derecha más baja.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x + 1) > (self.tablero - 1) or (self.y + 2) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x + 1
            self.y = self.y + 2
            return self.x, self.y
        return self.x + 1, self.y + 2

    def movInfIzqLar(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición inferior izquierda más baja.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x - 1) < 0 or (self.y + 2) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x - 1
            self.y = self.y + 2
            return self.x, self.y
        return self.x - 1, self.y + 2

    def movInfDerCor(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición inferior derecha menos baja.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x + 2) > (self.tablero - 1) or (self.y + 1) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x + 2
            self.y = self.y + 1
            return self.x, self.y
        return self.x + 2, self.y + 1

    def movInfIzqCor(self, realizaMov=False):
        """Metodo encargado de mover el caballo a la posición inferior izquierda menos baja.
            :parameter:
                - realizaMov: Booleano encargado de confirmar el movimiento."""
        if (self.x - 2) < 0 or (self.y + 1) > (self.tablero - 1):
            return False
        if realizaMov:
            self.x = self.x - 2
            self.y = self.y + 1
            return self.x, self.y
        return self.x - 2, self.y + 1

    def movimientosPosibles(self):
        """Metodo encargado de entregar una lista con los posibles movimientos del caballo."""
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
        """Metodo encargado de setear la coordenada X de la posición del caballo.
            :parameter:
                - x: Nueva posición X."""
        self.x = x

    def getX(self):
        """Metodo encargado de obtener la coordenada X de la posición del caballo."""
        return int(self.x)

    def setY(self, y):
        """Metodo encargado de setear la coordenada Y de la posición del caballo.
            :parameter:
                - y: Nueva posición Y."""
        self.y = y

    def getY(self):
        """Metodo encargado de obtener la coordenada Y de la posición del caballo."""
        return int(self.y)

    def setXY(self, x, y):
        """Metodo encargado de setear las coordenada X e Y de la posición del caballo.
            :parameter:
                - x: Nueva posición X.
                - y: Nueva posición Y."""
        self.x = x
        self.y = y

    def getXY(self):
        """Metodo encargado de obtener las coordenada X e Y de la posición del caballo."""
        return int(self.x), int(self.y)

    def setTablero(self, n):
        """Metodo encargado de setear la dimensión del tablero.
            :parameter:
                - n: Nueva dimensión del tablero."""
        self.tablero = n

    def getTablero(self):
        """Metodo encargado de obtener la dimensión del tablero."""
        return int(self.tablero)