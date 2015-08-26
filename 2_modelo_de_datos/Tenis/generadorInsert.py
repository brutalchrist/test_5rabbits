# -*- coding: utf-8 -*-
"""Pequeño Script para generar 20 Players con Rankings aleatorios únicos."""

from random import randint

ARCHIVOSALIDA = 'insertPlayers.sql'
listaInserts = []

while True:
    if len(listaInserts) == 20:
        break
    numeroRandom = randint(1, 100)
    if(numeroRandom in listaInserts):
        continue
    listaInserts.append("insert into PLAYERS values (\'NoName\', \'NoCountry\', " + str(numeroRandom) + ");")

salida = open(ARCHIVOSALIDA, 'w')

for insert in listaInserts:
    salida.write(insert + '\n')

print "Inserts generados en " + ARCHIVOSALIDA