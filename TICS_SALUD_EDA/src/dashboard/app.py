# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import os, sys
#C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The Bridge\Gina\TICS_SAlUD_EDA\src\
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

bbdd_path = os.path.dirname(path) + os.sep + "data" + os.sep + "Base_completa.csv"
print(bbdd_path)

menu = st.sidebar.selectbox('Menu:',
            options=["Bienvenidos/as", "Base de datos", "Load Dataframe Columns"])

if menu == 'Bienvenidos/as':
    st.title('TICS y SALUD')
    st.write('Bienvenidos a la preentación del proyecto sobre Tecnologías de la información y la comunicación y su asociación con diferentes parámetros de salud ')

if menu == 'Base de datos':
    BBDD = pd.read_csv(bbdd_path)
    st.table(BBDD) 


if menu == 'Normal Dataframe':
    features = create_sliders()
    features_df  = pd.DataFrame([features])
    st.table(features_df)  