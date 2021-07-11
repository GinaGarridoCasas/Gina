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

bbdd_path = os.path.dirname(path) + os.sep + "data" + os.sep + "Bases_trabajo" + os.sep +"ENS_2017_C_agr.csv"
print(bbdd_path)

# Crea el menú de la página web con las diferentes opciones que queremos que incluya: Bienvenida, mostrar el data frame, conexión con flask

menu = st.sidebar.selectbox('Menu:',
            options=["Título", "Abstract","Base de datos","Predicción","leer json"])

# Damos un título a la pestaña del menú: Título

if menu == 'Título':
    st.title('Comparación de modelos de Machine learning en la prediccion de la salud a patir de determinantes de salud')
    
# Damos un texto a la pestaña del menú: Abstract
    
if menu == 'Abstract':
    st.write('Abstract:' 
    'Objetivo: Identificar el mejor modelo de machine learning o deep learning para predecir la salud a partir de determinantes de salud,' 
    'Fuente de datos: Encuesta Nacional de salud (2017),'
    'Variables utilizadas: VD: salud percibida, VI: Prácticas preventivas, Características físicas, Actividad física, Alimentación, Higiene dental, Consumo de tabaco, Consumo de alcohol, Apoyo afectivo y personal, sociodemográficas'
    'Modelos de Machine learning y deep learning utilizados: Lineal regression, polynomial regression y SVR, logistic regression, K_neigbors y SVR, DecissionTreeRegressor, DecissionTreeClassifier, RandomForestRegressor y RandomForestClassifier, RNN'
    'Conclusiones: Los modelos con mejores resultados fueron: SVC y DecissionTreeClassifier, Las variables con mayor peso en la predicción: Edad_agrupada, actividad económica actual, nivel de estudios, estado Civil, frecuencia de actividad física actual, frecuencia de consumo de carne, frecuencia de consumo de verduras, ensaladas y hortalizas,' 
    'frecuencia de consumo de alcohol y apoyo afectivo y personal de amigos y familiares'
    'Con la aplicación conjunta de ambos modelos (modelo: Voting Hard) se obtiene una precisión en la predicción de 0.9487 (accuracy_score) utilizando únicamente las variables de mayor peso detectadas.')

# Indicamos en la pestaña de Base de datos que ha de mostrar el data frame de nuestro base de datos
if menu == 'Base de datos':
    BBDD = pd.read_csv('C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The_Bridge\Gina\jorgina_garrido_cmmlsds_apr\data\Bases_trabajo\ENS_2017_valida_agr.csv')
    st.table(BBDD)

# Indicamos en la pestaña de Predicción un pequeño cuestionario a rellenar en el que se recoge información de las variables incluidas en el modelo (VI). Ha de predecir la VD
if menu == 'Predicción':
    cuestionario = pd.read_csv(bbdd_path)
    aplicación_modelo = 
    

# En la tercera pestaña, leemos nuestro fichero de datos en json desde Flask

if menu == 'leer json':
    features_df  = pd.read_json("http://localhost:6060/obtener_json?token_id=H13297422")
    st.table(features_df)  
