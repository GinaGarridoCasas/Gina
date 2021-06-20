# Pasar una columna a índice

TICS_2017.set_index('CCAA', inplace = True)

# Pasar la variable índice a columna

TICS_2017['index'] = TICS_2017.index

