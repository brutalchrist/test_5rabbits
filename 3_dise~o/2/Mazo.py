#-*- coding: utf-8 -*-
"""
Problema 2 del Test de diseño para LemonTech.\n
<Diseñe un mazo de cartas (orientado a objetos) con propiedades y métodos básicos que considere para ser utilizado en distintas aplicaciones que utilicen cartas.>
"""


class Mazo(object):
    def __init__(self, nombreMazo,  nCartasMazo=60, listaCartasMazo=[]):
        """Inicializador de la clase.
            :parameter:
                - nombreMazo: Nombre del mazo
                - nCartasMazo: Número de cartas del mazo (60 por defecto).
                - listaCartasMazo: Lista con las cartas del mazo (vacia por defecto)"""
        # Se definen los atributos estaticos de un mazo
        self.nombreMazo = nombreMazo
        self.nCartasMazo = nCartasMazo
        self.listaCartasMazo = listaCartasMazo

        # Se definen los atributos dinámicos de un mazo
        self.listaBiblioteca = self.listaCartasMazo
        self.listaPozoDescarte = []

    # Acciones
    def robarCartaBiblioteca(self, nCartas=1):
        """Método encargado de obtener la o las cartas de la la parte superior de la Biblioteca.
            :parameter:
                - nCartas: Número de cartas a robar (1 por defecto)."""
        return "Se ha robado la carta: " + self.listaBiblioteca.pop()

    def enviarCartasPozoDescarte(self, listaCartas):
        """Método encargado de enviarr una o unas cartas al Pozo de descarte.
            :parameter:
                - listaCartas: Lista las cartas a enviar."""
        return "Enviada la(s) carta(s): " + str(listaCartas) + " al Pozo de descarte"

    def buscarCartasBiblioteca(self, listaIndexs):
        """Método encargado de obtener la o las cartas de una posición especifica de la Biblioteca.
            :parameter:
                - listaIndexs: Lista con las posiciones de las cartas a obtener."""
        return "La(s) carta(s) con index(s): " + str(listaIndexs)

    def buscarCartasPozoDescarte(self, listaIndexs):
        """Método encargado de obtener la o las cartas de una posición especifica del Pozo de descarte.
            :parameter:
                - listaIndexs: Lista con las posiciones de las cartas a obtener."""
        return "La(s) carta(s) con index(s): " + str(listaIndexs)

    def devolverCartasBiblioteca(self, listaCartas):
        """Método encargado de devolver una o unas cartas en la parte superior de la Biblioteca.
            :parameter:
                - listaCartas: Lista las cartas a devolver."""
        # Si para robar utilizamos push para devolver utilizamos append
        print "Agregada(s) la(s) carta(s): " + str(listaCartas) + " a la parte superior de la Biblioteca"

    def devolverCartasBibliotecaAleatorio(self, listaCartas):
        """Método encargado de devolver una o unas cartas aleatoriamente a la Biblioteca.
            :parameter:
                - listaCartas: Lista las cartas a devolver."""
        print "Agregada(s) la(s) carta(s): " + str(listaCartas) + " aleatoriamente a la Biblioteca"

    def cartasRestantesBiblioteca(self):
        """Método encargado retornar el número de cartas restantes en la Biblioteca."""
        return len(self.listaBiblioteca)

    def barajarBiblioteca(self):
        """Método encargado de barajar la Biblioteca."""
        print "Biblioteca barajada"

    def barajarPozoDescarte(self):
        """Método encargado de barajar el Pozo de descarte."""
        print "Pozo de descarte barajada"


    # Comprobaciones
    def isBibliotecaVacia(self):
        """Método encargado de retornar verdadero si la Biblioteca está vacia."""
        if len(self.listaBiblioteca) <= 0:
            return True
        return False

    def isPozoDescarteVacio(self):
        """Método encargado de retornar verdadero si el Pozo de descarte está vacio."""
        if len(self.listaBiblioteca) <= 0:
            return True
        return False


    # Getters & Setters
    def getNombreMazo(self):
        """Método encargado de retornar el nombre del Mazo."""
        return self.nombreMazo

    def setNombreMazo(self, nombreMazo):
        """Método encargado de setear el nombre del Mazo.
            :parameter:
                - nombreMazo: Nombre del mazo."""
        self.nombreMazo = nombreMazo

    def getNCartasMazo(self):
        """Método encargado de retornar el número de cartas del Mazo."""
        return self.nCartasMazo

    def setNCartasMazo(self, nCartasMazo):
        """Método encargado de setear el número de cartas del Mazo.
            :parameter:
                - nCartasMazo: Número de cartas del mazo."""
        self.nCartasMazo = nCartasMazo

    def getListaCartasMazo(self):
        """Método encargado de retornar la lista de cartas del Mazo."""
        return self.listaCartasMazo

    def setListaCartasMazo(self, listaCartasMazo):
        """Método encargado de setear la lista de cartas del Mazo.
            :parameter:
                - listaCartasMazo: Lista de cartas del Mazo."""
        self.listaCartasMazo = listaCartasMazo

    def getListaBiblioteca(self):
        """Método encargado de retornar la lista de cartas de la Biblioteca."""
        return self.listaBiblioteca

    def setListaBiblioteca(self, listaBiblioteca):
        """Método encargado de setear la lista de cartas de la Biblioteca. Esta lista suele ser la misma del Mazo, por ejemplo:
            magicMazo.setListaBiblioteca(magicMazo.getListaCartasMazo())
            :parameter:
                - listaBiblioteca: Lista de cartas de la Biblioteca."""
        self.listaBiblioteca = listaBiblioteca

    def getListaPozoDescarte(self):
        """Método encargado de retornar la lista de cartas del Pozo de descarte."""
        return self.listaPozoDescarte

    def setListaPozoDescarte(self, listaPozoDescarte):
        """Método encargado de setear la lista de cartas del Pozo de descarte.
            :parameter:
                - listaBiblioteca: Lista de cartas de la Biblioteca."""
        self.listaPozoDescarte = listaPozoDescarte