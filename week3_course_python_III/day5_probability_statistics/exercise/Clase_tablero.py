class tablero:
    def __init__ (self, nombre, filas = 10, columnas = 10, casillas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.casillas = casillas

    def casillas (self, casillas):
        casillas = self.casillas 
        
        return casillas

    def mostrar(self):
        print (' ')

    # instancias

    tablero_vacio = tablero (nombre = "tab_vacio", filas = 10, columnas = 10, casillas = )
    tablero_barcos_propio = tablero (nombre = "tab_barcos", filas = 10, columnas = 10, casillas = )
    tablero_partida_contrincante = tablero (nombre = "tab_partida", filas = 10, columnas = 10, casillas = )




