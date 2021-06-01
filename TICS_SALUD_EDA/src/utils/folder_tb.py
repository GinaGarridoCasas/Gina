import pandas as pd

def leer_fichero_csv (df):
    TICS_2017 = pd.read_csv(df, sep =';')

    return TICS_2017

def crear_fichero_json(df):
    csv_data = pd.read_csv("df", sep = ",")
    csv_data.to_json("df.json", orient = "records")

    return df.json



