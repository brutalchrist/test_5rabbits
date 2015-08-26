# -*- coding: utf-8 -*-
"""Pequeño Script para generar 20 Players con Rankings aleatorios únicos."""

from random import randint

ARCHIVOSALIDA = 'insertPlayers.sql'
listaInserts = []

while True:
    if len(listaInserts) == 20:
        break

    numeroRandom = randint(1, 100)
    if int(numeroRandom) in listaInserts:
        continue

    listaInserts.append(numeroRandom)

salida = open(ARCHIVOSALIDA, 'w')

for insert in listaInserts:
    salida.write("insert into PLAYERS values (\'NoName\', \'NoCountry\', " + str(insert) + ");\n")

print "Inserts generados en " + ARCHIVOSALIDA