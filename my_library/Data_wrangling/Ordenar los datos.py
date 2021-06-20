# ordenar los datos en base a una columna (index)

TICS_2017 = TICS_2017.sort_index()

# reseteamos el índice

TICS_2017 = TICS_2017.reset_index(drop = True)