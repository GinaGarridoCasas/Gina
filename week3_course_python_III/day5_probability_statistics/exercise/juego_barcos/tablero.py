import json
import pandas as pd
import numpy as np 
import random as rd 


class Tablero:


    def __init__(self, columnas, filas, nombre):
        self.columnas = columnas
        self.filas = filas
        self.nombre = nombre

        fila = ['~'] * self.filas
        tablero = {i: fila for i in range(1, self.columnas + 1)}
        index = list(range(1,11))
        tablero = pd.DataFrame(tablero, index=index)

        self.tablero = tablero


    def comprobar_tablero(self):
        """
        Muestra por pantalla el estado del tablero.
        """
        print(f'El estado actual del tablero de {self.nombre} es: \n')
        print(self.tablero, '\n')


    def comprobar_jugada(self, casilla):
        """

        """
        if self.tablero.loc[casilla[0]][casilla[1]] == '#':
            acierto = 'barco'
            print('¡Acierto! El disparo ha dado en un barco')
        elif self.tablero.loc[casilla[0]][casilla[1]] == '~':
            acierto = 'agua'
            print('El disparo ha dado en agua')
        else:
            acierto = 'ya atacado'
            print('La casilla elegida ya se había bombardeado')

        return acierto


    def actualizar_jugada(self, acierto, casilla):
        """

        """
        if acierto == 'barco':
            self.tablero.loc[casilla[0]][casilla[1]] = 'x'
        elif acierto == 'agua':
            self.tablero.loc[casilla[0]][casilla[1]] = 'o'

        return self.tablero


    def actualizar_barco(self, casillas):
        """

        """
        errores = False
        for casilla in casillas:
            if self.tablero.loc[casilla[1]][casilla[0]] == '#':
                errores = True
                break

        if not errores:
            for casilla in casillas:
                self.tablero.loc[casilla[1]][casilla[0]] = '#'
            self.comprobar_tablero()    
        else:
            print(f'Has elegido una posición que ya tiene un barco. Vuelve a introducir la posición del barco')
        
        return self.tablero, errores

    
    def guarda_json(self, nombre_archivo):
        """

        """
        with open(nombre_archivo, 'w+') as outfile:
            tablero_json= self.tablero.to_dict('index')
            json.dump(tablero_json, outfile, indent=4)


    def comprobar_estado_aciertos(self):
        """
        Comprueba si hay suficientes aciertos para ganar
        """
        ganador = False
        
        array = self.tablero.to_numpy()
        aciertos = np.sum(array == 'x')
        if aciertos == 2:
            ganador = True
        
        return ganador











# if __name__ == 'main':
# fila = ['~'] * 10
# tablero = {i: fila for i in range(1, 10 + 1)}
# index = list(range(1,11))
# tablero = pd.DataFrame(tablero, index=index)
# tablero.loc[1, 1] = 'x'
# tablero.loc[1, 2] = 'x'
# ganador = False

# array = tablero.to_numpy()
# aciertos = np.sum(array == 'x')
# if aciertos == 2:
#     ganador = True

# print(ganador)