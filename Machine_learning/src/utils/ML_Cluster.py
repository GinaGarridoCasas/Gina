
# Tabla de contingencia (valores absolutos)
def crosstabs (df,col1,col2):
    Cluster_col2 = pd.crosstab(df['col1'],df['col2'],margins = False)
    
    return Cluster_col2


# Tabla de contingencia (% columnas)
def crosstabs (df,col1,col2):
    Cluster_col2 = pd.crosstab(index =df['col1'],columns =df['col2']).apply(lambda r: r/r.sum() *100,
                                axis=0)
    return Cluster_col2


# Tabla de contingencia (% filas)
def crosstabs (df,col1,col2):
    Cluster_col2 = pd.crosstab(index =df['col1'],columns =df['col2']).apply(lambda r: r/r.sum() *100,
                                axis=1)
    return Cluster_col2