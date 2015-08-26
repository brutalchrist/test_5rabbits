#-*- coding: utf-8 -*-
"""Script de prueba para probar la clase Mazo"""

from Mazo import Mazo

if __name__ == '__main__':
    listaCartas = ["Contrahechizo", "Mana azul", "Mana azul", "Darting Merfolk"]

    magicMazo = Mazo("Mazo prueba", 4, listaCartas)

    magicMazo.setListaBiblioteca(magicMazo.getListaCartasMazo())
    print "Nombre: " + magicMazo.getNombreMazo() + ", Número de cartas: " + \
          str(magicMazo.getNCartasMazo()) + "\nLista de Cartas: " + str(magicMazo.getListaBiblioteca())