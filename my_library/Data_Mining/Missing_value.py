# Creamos la variable que nos cuenta los missing
missing_values_count = Base_TICS_Salud.isnull().sum()

# variable de missing creada para cada columna
missing_values_count

# missing para cada columna
missing_values_count[0:10]

# Calculamos el % de valores missing sobre el total de valores
    # Total de celdas
    total_cells = np.product(Nombre_data.shape)

    # Total de missing sumando todos los valores de la variable que contiene missing para cada columna
    total_missing = missing_values_count.sum()

    # Calculamos el %
    total_missing/total_cells*100 
    
# Calcular el ratio de NaN por columna

na_ratio = ((df.isnull().sum() / len(df))*100).sort_values(ascending = False)

# Tratamiento de missing value

    # Eliminar filas con valor missing
    df.dropna() 

    # eliminar las variables (columnas) que tengan al menos un dato missing

        # seleccionamos las columnas con algún valor missing
        Columnas_con_valor_na = df.dropna(axis=1)

        # vemos las columnas que han quedado
        Columnas_con_valor_na.head()

    # Sustituir missing por otro valor, ej. 0
    df.fillna(0)

    # Sustituir missing por otro el valor seleccionado en diferentes columnas
    df = df.fillna({'magnesium':100, 'alcohol':10})



     