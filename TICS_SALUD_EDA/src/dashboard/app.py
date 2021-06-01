# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import os, sys

#C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The Bridge\Gina\TICS_SAlUD_EDA\src\
path = os.path.dirname(os.path.dirname(__file__))  # nos da la ruta en la que estamos
sys.path.append(path)

# indicamos el lugar donde se encuentra el archivo que queremos leer partiendo desde donde queremos leerlo (ruta en la que estamos situados)

bbdd_path = os.path.dirname(path) + os.sep + "data" + os.sep + "Base_completa.csv"
print(bbdd_path)

# Crea el menú de la página web con las diferentes opciones que queremos que incluya: Bienvenida, mostrar el data frame, conexión con flask

menu = st.sidebar.selectbox('Menu:',
            options=["Bienvenidos/as", "Base de datos", "Load Dataframe Columns"])

# Damos un título y un texto a la pestaña del menú: Bienvenida

if menu == 'Bienvenidos/as':
    st.title('TICS y SALUD')
    st.write('Bienvenidos a la presentación del proyecto sobre Tecnologías de la información y la comunicación y su asociación con diferentes parámetros de salud')

# Indicamos en la pestaña de Base de datos que ha de mostrar el data frame de nuestro base de datos
if menu == 'Base de datos':
    BBDD = pd.read_csv(bbdd_path)
    st.table(BBDD) 

# En la tercera pestaña, leemos nuestro fichero de datos en json desde Flask

if menu == 'leer json':
    features = create_sliders()
    features_df  = pd.read_json("http://localhost:6060/obtener_json?token_id=H13297422")
    st.table(features_df)  
