# Función para calcular los porcentajes de missing en cada variable

def Porcentaje_missing_columna (df):
    na_ratio = ((df.isnull().sum() / len(df))*100)

    return na_ratio

# Visualización de outliers
def visualizacion_outliers (df):
    for i in df:
        plt.figure(figsize=(15,8))
        boxplot = TICS_Salud.boxplot(column=['ADSL','cable_fibra optica','otras conexiones','conexion movil_dispositivo_mano','movil_USB'])
        
        return boxplot.plot()
 
    plt.savefig("../reports/Outliers/ENS_2017.jpg", bbox_inches='tight') # para archivar el gráfico como jpg
  
  
  
  
# Función para determinar el porcentaje de outlieres en cada columna ???

def get_iqr_values(df_in, col_name):
    median = df_in[col_name].median()
    q1 = df_in[col_name].quantile(0.25) # 25th percentile / 1st quartile
    q3 = df_in[col_name].quantile(0.75) # 75th percentile / 3rd quartile
    iqr = q3-q1 #Interquartile range
    minimum  = q1-1.5*iqr # The minimum value or the |- marker in the box plot
    maximum = q3+1.5*iqr # The maximum value or the -| marker in the box plot
        
    return median, q1, q3, iqr, minimum, maximum

def count_outliers(df_in, col_name):

    minimum, maximum = get_iqr_values(df_in, col_name)
    df_outliers = df_in.loc[(df_in[col_name] <= minimum) | (df_in[col_name] >= maximum)]
        
    return df_outliers.shape[0]


def outliers_columnas(df):
    f = []
    for i in df:
        median = df[i].median()
        q1 = df[i].quantile(0.25) # 25th percentile / 1st quartile
        q3 = df[i].quantile(0.75) # 75th percentile / 3rd quartile
        iqr = q3-q1 #Interquartile range
        minimum  = q1-1.5*iqr # The minimum value or the |- marker in the box plot
        maximum = q3+1.5*iqr # The maximum value or the -| marker in the box plot
 
        if i > maximum:
            f.append(i)
        elif i < minimum:
            f.append(i)
    
    sums = len(f)
    pros = len(f)/len(df)*100

    d = {'IQR':iqr,
         'Cuartil75':maximum,
        'Cuartil25':minimum,
        'Suma de outliers': sums,'Porcentaje de outliers': pros}
    d = pd.DataFrame(d.items(),columns = ['sub','values'])
    
    return(d)
           
        