import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Función para calcular los porcentajes de missing en cada variable

def Porcentaje_missing_columna (df):
    na_ratio = ((df.isnull().sum() / len(df))*100)

    return na_ratio

 
# Función para eliminar correlaciones repetidas y las de la diagonal

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

# Función para obtener el Top x de correlaciones más altas que queramos

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

# función para visualizar correlaciones. Heatmap
def heatmap(x):
    f, ax = plt.subplots(figsize=(13, 10))
    sns.heatmap(x.corr(),
           vmin = -1,
           vmax = 1,
            annot = True,
           linewidths = .5)
    return f, ax


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
           
        