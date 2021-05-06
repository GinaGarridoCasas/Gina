import json
import re
from random import randint
import numpy as np 
import pandas as pd 
from barco import Barco
from tablero import Tablero


def elegir_una_casilla():
    """

    """
    jugada = input('Inserte coordenadas a atacar. El formato es \"0x8\" con 0 para las filas y 8 para las columnas: ')
    patron_casilla = r'^[1-9]|10x[1-9]|10$'   # REVISAR FALLO!!
    
    while True:
        try:
            assert(re.search(patron_casilla, jugada))
            break
        except AssertionError:
            print('La casilla introducida no está en el formato solicitado. Por favor introduce un valor tipo \"5x6\".')
            jugada = input ('Inserte coordenadas a atacar: ')

    return jugada


def atacar(tablero, tablero_contrincante):
    """
    Coge casillas jugada por el jugador, actualiza el tablero y lo muestra.
    """
    patron_numeros = r'\d\d|\d'
    jugada = elegir_una_casilla()
    casilla = [int(i) for i in re.findall(patron_numeros, jugada)]

    acierto = tablero.comprobar_jugada(casilla)
    tablero_contrincante = tablero_contrincante.actualizar_jugada(acierto, casilla)
    tablero = tablero.actualizar_jugada(acierto, casilla)

    return tablero_contrincante, tablero


def sortear_turno(jugador, contrincante):
    """

    """
    while True:
        comienzo1 = randint(1, 7)
        comienzo2 = randint(1, 7)
        print(f'{jugador} ha sacado un {comienzo1}')
        print(f'{contrincante} ha sacado un {comienzo2}')
        if comienzo1 > comienzo2:
            primer_jugador = True
            print(f'{jugador} empieza')
            return primer_jugador
        elif comienzo1 < comienzo2:
            primer_jugador = False
            print(f'{contrincante} empieza')
            return primer_jugador
        else:
            print('Los judadores han sacado el mismo número. Se vuelve a sortear')


def colocar_barco(barco, tablero):
    """

    """
    while True:
        print(f'Inserte la posición del {barco.nombre} {barco.casillas}')
        tabla, errores = barco.colocar_barco(tablero)
        if not errores: 
            tablero = tabla
            break
    
    return tablero


def colocar_todos_barcos(tablero):
    """

    """
    barcos_de_2 = [Barco(2, f'barco{i}') for i in range(1, 5)]
    barcos_de_3 = [Barco(3, f'barco{i}') for i in range(5, 9)]
    barcos_de_4 = [Barco(4, f'barco{i}') for i in range(9, 11)]
    barco_de_5 = [Barco(5, 'barco10')]
    todos_barcos = barcos_de_2 + barcos_de_3 + barcos_de_4 + barco_de_5

    for barco in todos_barcos:
        colocar_barco(barco, tablero)


def colocar_barcos_prueba(tablero):
    """

    """
    barco_de_2 = Barco(2, 'barco1')
    colocar_barco(barco_de_2, tablero)


def elegir_opciones(jugador):
    """

    """
    print(f"""Qué opción eliges, {jugador}:
        1. Elegir la posición de los barcos
        2. Cargar una configuración de barcos ya guardada""")

    while True:
        opcion = input('Introduce la opicón que prefieres: ')
        if opcion == '1':
            tablero = Tablero(10, 10, jugador)
            tablero_contrincante = Tablero(10, 10, f'Contrincante {jugador}')
        elif opcion == '2':
            
            
