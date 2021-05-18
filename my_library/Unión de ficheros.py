# unir dos ficheros por columnas. Añadir columnas
all_series_col = pd.concat([first, second, third], axis=1)

   
# unir dos ficheros con las mismas columnas. añadir filas  
bigcolumn = pd.concat([first, second, third])
bigcolumn.set_axis(['bigcolumn'],axis='columns', inplace=True)

all_data = pd.concat([data1, data2])
all_data
