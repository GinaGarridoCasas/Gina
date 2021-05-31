
  # función que calcula en la columna que se especifique la mediana, el primer y tercer cuartil, el rango intercuartil, y el valor mínimo y máximo. Cualquier valor por encima del mínmo y máximo es un valor atípico\n",

    def get_iqr_values(df_in, col_name):
        median = df_in[col_name].median()
        q1 = df_in[col_name].quantile(0.25) # 25th percentile / 1st quartile
        q3 = df_in[col_name].quantile(0.75) # 75th percentile / 3rd quartile
        iqr = q3-q1 #Interquartile range
        minimum  = q1-1.5*iqr # The minimum value or the |- marker in the box plot
        maximum = q3+1.5*iqr # The maximum value or the -| marker in the box plot
        
        return median, q1, q3, iqr, minimum, maximum

    
# Función para imprimir en un texto los valores de la mediana, cuartiles 25 y 75 recorrido intercuartílico y valores mínmo y máximo\n",
    
    def get_iqr_text(df_in, col_name):
        median, q1, q3, iqr, minimum, maximum = get_iqr_values(df_in, col_name)
        text = f"median={median:.2f}, q1={q1:.2f}, q3={q3:.2f}, iqr={iqr:.2f}, minimum={minimum:.2f}, maximum={maximum:.2f}"
        
        return text

# función para eliminar los outliers
    def remove_outlier(df_in, col_name):
        q1 = df_in[col_name].quantile(0.25)
        q3 = df_in[col_name].quantile(0.75)
        iqr = q3-q1 #Interquartile range
        fence_low  = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
        return df_out


# funcion para contar los outliers
    def count_outliers(df_in, col_name):
        minimum, maximum = get_iqr_values(df_in, col_name)
        df_outliers = df_in.loc[(df_in[col_name] <= minimum) | (df_in[col_name] >= maximum)]
        
        return df_outliers.shape[0]
   

# esta función llama a la de remove repetidamente hasta que se hayan eliminado todos los valores atípicos
def remove_all_outliers(df_in, col_name):
    loop_count = 0
    outlier_count = count_outliers(df_in, col_name)

    while outlier_count > 0:
        loop_count += 1

        if (loop_count > 100):
            break

        df_in = remove_outliers(df_in, col_name)
        outlier_count = count_outliers(df_in, col_name)
    
    return df_in
