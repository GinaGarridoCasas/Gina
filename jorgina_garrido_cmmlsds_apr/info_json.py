import json
import os

data = {}
data['nombre_proyecto'] = 'Comparación de modelos de machine learning y deep learning en la predicción de la salud a partir de determinantes de salud'
data['autora'] = 'Jorgina Garrido Casas'
data['linkedin'] = ''
data['mail'] = 'jorginagc@gmail.com'
data['Título_proyecto'] = 'Comparación de modelos de machine learning y deep learning en la predicción de la salud a partir de determinantes de salud'
data['autora'] = 'Jorgina Garrido Casas'
data['Descripción_proyecto'] = 'A partir de la identificación de clusters, se comparan modelos de regresión, de clasificación, mixtos (DecisionTree y RandomForest) y redes neuronales. Una vez identificados los mejores se utiliza Gridsearch para determinar entre ellos cual es el que mejores resultados obtiene y se prueba con el algoritmo voting si mejoran los resultados utilizando conjuntamente los diferentes modelos con mejores resultados'
data['flask_port'] = '6060'
data['streamlit_port'] = ''
data['python_libraries_used'] = 'pandas, numpys, matplotlib, seaborn, sklearn, tensorflow, keras' 


dir = 'C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The Bridge\Gina\jorgina_garrido_cmmlsds_apr\documentation' 
file_name = "info.json"

with open(dir, 'w+') as outfile:
    json.dump(file_name, outfile, indent=4)

  