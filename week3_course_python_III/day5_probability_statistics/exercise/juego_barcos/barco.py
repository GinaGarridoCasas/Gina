import re


class Barco:

    def __init__(self, longitud, nombre):
        self.longitud = longitud
        self.nombre = nombre
        self.casillas = f'({longitud}x1)'


    def posicion_barco(self):
        """
        Pide la posición del barco por pantalla y comprueba que tenga el formato adecuado.
        Retorna la posición del barco:
        """
        barco = input ('Teclea la posición elegida: ')
        patron= r'^[1-9]|10[vh][1-9]|10:[1-9]|10$'
    
        while True:
            try:
                assert(re.search(patron, barco))
                break
            except AssertionError:
                print('La posición introducida no está en el formato solicitado. Por favor introduce un valor tipo \"4h9:10\".')
                barco = input ('Teclea la posición elegida: ')

        return barco


    def posicion_y_logitud_barco(self):
        """
        La función recoge los números de una entrada por pantalla(fila o columna y las casillas)
        Cálcula la longitud para comprobar que coincide con la solicitada como parámetro y devuelve 
        las posiciones del tablero y si se colocar en horizontal o vertical.
        """
        patron_numeros = r'\d\d|\d'

        while True:
            barco = self.posicion_barco()

            posiciones_numericas = [int(i) for i in re.findall(patron_numeros, barco)]  

            longitud_barco = len(range(posiciones_numericas[1], posiciones_numericas[2] + 1))  

            if longitud_barco == self.longitud:                 
                patron_v_vs_h = r'v|h'
                v_vs_h = re.findall(patron_v_vs_h, barco)
                return posiciones_numericas, v_vs_h         
            else:
                print(f'El barco no tiene la longitud necesaria. Tiene que ocupar {self.longitud} casillas. Introduce el barco de nuevo')


    def colocar_barco(self, tablero, aleatorio=False):
        """
        Pide que se coloque un barco en el tablero, representándolo con * en el lugar dónde se
        encuentra, en vez de agua (~). Si coincide con otro barco en alguna casilla pide que se 
        vuelva a colocar de nuevo.
        """
        # if aleatorio:
            # pass
        
        posiciones_numericas, v_vs_h = self.posicion_y_logitud_barco()
        
        if v_vs_h[0] == 'v':
            filas = range(posiciones_numericas[1], posiciones_numericas[2] + 1)
            columnas = posiciones_numericas[0]
            print('Tu barco se situa en el tablero.')
            
            casillas = [(columnas, i) for i in filas]

            tablero, errores = tablero.actualizar_barco(casillas)

        elif v_vs_h[0] == 'h':
            filas = posiciones_numericas[0]
            columnas = range(posiciones_numericas[1], posiciones_numericas[2] + 1)
            print('Tu barco se situa en el tablero.')

            casillas = [(i, filas) for i in columnas]    

            tablero, errores = tablero.actualizar_barco(casillas)
        
        return tablero, errores


