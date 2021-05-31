
# PREPARAR FICHEROS PARA UNIFICARLOS

import pandas as pd

def leer_fichero (df):
    TICS_2017 = pd.read_csv(df, sep =';')

    return TICS_2017

def borra_columna_index(dataframe):
    del dataframe["index"]
    return dataframe

def De_string_numérica (df, col_a, col_b, col_c, col_d, col_e):
    TICS_2017 = df.stack().str.replace(',','.').unstack()
    TICS_2017[['col_a', 'col_b','col_c', 'col_d', 'col_e']]= df[['col_a', 'col_b','col_c', 'col_d', 'col_e']].astype(float)

    return TICS_2017

def ordenar_índice (df):
    TICS_2017 = df.sort_index()

    return TICS_2017

def indice_columna (df):
    df['index'] = df.index

    return df


def resetear_índice(df):
    TICS_2017 = df.reset_index(drop = True)

    return TICS_2017


## CALIDAD DE LOS DATOS

def detectar_missing(df):
    missing_value_count = df.isnull().sum()

    return missing_value_count
   
def detectar_duplicados(df):
    Duplicados = df.duplicated()

    return Duplicados
   
import matplotlib.pyplot as plt


def detectar_outliers(df, col_a, col_b, col_c, col_d, col_e):
    plt.figure(figsize=(15,8))

    boxplot = df.boxplot(column=['col_a','col_b','col_c','col_d','col_e'])

    return boxplot.plot()


def eliminar_outlier(df_in, col_name):
    q1 = df_in[col_name].quantile(0.25)
    q3 = df_in[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out

# ANÁLISIS DE DATOS


def correlaciones (df):
    return df.corr()