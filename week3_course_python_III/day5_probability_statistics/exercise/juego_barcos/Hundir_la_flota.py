import json
import re
from random import randint
import numpy as np 
import pandas as pd 
from barco import Barco
from tablero import Tablero
from jugador import Jugador
import acciones
from datetime import datetime as dt 


print('Comienza la batalla de barcos: HUNDIR LA FLOTA')


nombre_1 = input('Introduce el nombre del primer jugador: ')
nombre_2 = input('Introduce el nombre del segundo jugador: ')

print(f"""Qué opción eliges, {nombre_1}:
        1. Elegir la posición de los barcos
        2. Cargar una configuración de barcos ya guardada""")




"""FALTA EL ACCESO A LAS OPCIONES"""




tablero_1 = Tablero(10, 10, nombre_1)
tablero_2 = Tablero(10, 10, nombre_2)

tablero_contrincante_1 = Tablero(10, 10, f'Contrincante {nombre_1}')
tablero_contrincante_2 = Tablero(10, 10, f'Contrincante {nombre_2}')



acciones.colocar_barcos_prueba(tablero_1)
now = dt.now()
tablero_1.guarda_json(f'{nombre_1}_{now.day}_{now.hour}_{now.minute}')
acciones.colocar_barcos_prueba(tablero_2)
tablero_2.guarda_json(f'{nombre_2}_{now.day}_{now.hour}_{now.minute}')



while True:
    print('Hay que sortear el comienzo del juego')
    lanzamiento = input('El que quiera lanzar el sorteo que escriba su nombre: ')
    if lanzamiento == nombre_1:
        primer_jugador = acciones.sortear_turno(nombre_1, nombre_2)
        break
    elif lanzamiento == nombre_2:
        primer_jugador = acciones.sortear_turno(nombre_1, nombre_2)
        break
    else:
        print('El nombre introducido no es correcto')



""" FALTA AQUÍ QUE CADA UNO CARGE EL ESTADO INICIAL DEL OTRO"""


while True:
    if (lanzamiento == nombre_1 and primer_jugador) or (lanzamiento == nombre_2 and not primer_jugador):
        acciones.atacar(tablero_1, tablero_contrincante_1)
        print('Después de la jugada estos son tus disparos')
        tablero_contrincante_1.comprobar_tablero()
        now = dt.now()
        tablero_1.guarda_json(f'{nombre_1}_{now.day}_{now.hour}_{now.minute}')
        ganador = tablero_contrincante_1.comprobar_estado_aciertos()
        if not ganador:
            acciones.atacar(tablero_2, tablero_contrincante_2)
            print('Después de la jugada estos son tus disparos')
            tablero_contrincante_2.comprobar_tablero()
            now = dt.now()
            tablero_2.guarda_json(f'{nombre_2}_{now.day}_{now.hour}_{now.minute}')
            ganador = tablero_contrincante_2.comprobar_estado_aciertos()
            if ganador:
                print(f'{nombre_2} ha ganado la partida')
                break
        else:
            print(f'{nombre_1} ha ganado la partida')
            break
    else:
        acciones.atacar(tablero_2, tablero_contrincante_2)
        print('Después de la jugada estos son tus disparos')
        tablero_contrincante_2.comprobar_tablero()
        now = dt.now()
        tablero_2.guarda_json(f'{nombre_2}_{now.day}_{now.hour}_{now.minute}')
        ganador = tablero_contrincante_2.comprobar_estado_aciertos()
        if not ganador:
            acciones.atacar(tablero_1, tablero_contrincante_1)
            print('Después de la jugada estos son tus disparos')
            tablero_contrincante_1.comprobar_tablero()
            now = dt.now()
            tablero_1.guarda_json(f'{nombre_1}_{now.day}_{now.hour}_{now.minute}')
            ganador = tablero_contrincante_1.comprobar_estado_aciertos()
            if ganador:
                print(f'{nombre_1} ha ganado la partida')
                break


















