import pandas as pd

def leer_fichero (df):
    TICS_2017 = pd.read_csv(df, sep =';')

    return TICS_2017

def transponer_filas (df, col_a, col_b):
    comunidades_autonomas = df["col_a"].unique()
    comunidades_autonomas_ordenada = sorted(list(comunidades_autonomas)) 
    comunidades_autonomas_ordenada.insert(0, comunidades_autonomas_ordenada[-1])
    comunidades_autonomas_ordenada.pop()

    tipo_conex = df["col_b"].unique()
    diccionario_final = {}
    for conex in tipo_conex:
        diccionario_final[conex] = []
    for row in df.iterrows():
        comunidad = row[1][0]
        tipo_conex = row[1][1]
        valor = row[1][2]
        diccionario_final[tipo_conex].append(valor)

    TICS_2017 = pd.DataFrame(diccionario_final, index=comunidades_autonomas_ordenada)

    return TICS_2017