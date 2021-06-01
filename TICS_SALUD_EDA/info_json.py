import json
import os

data = {}
data['nombre_proyecto'] = '¿Son más saludables las poblaciones con mejores conexiones a TICS?'
data['autora'] = 'Jorgina Garrido Casas'
data['linkedin'] = ''
data['mail'] = ''
data['Título_proyecto'] = '¿Son más saludables las poblaciones con mejores conexiones a TICS?'
data['Descripción_proyecto'] = 'El objetivo es conocer la asociación entre el tipo de conexión a TICS y la salud de la población. Se encuentran asociaciones positivas entre mayor conexión por cable o fibra óptica y dolor de espalda crónico cervical y lumbar, migraña, depresión y otros problemas de salud mental. Esta asociación está modulada por variables intermedias diferentes a: renta media del hogar, nivel de estudios, tasa de paro, índice de masculinidad o edad entre 25 y 59 años que sería de interés estudiar en futuros estudios, tales como habilidades digitales, ocupación mayoritaria de la población, ...
 '
data['flask_port'] = ''
data['streamlit_port'] = ''
data['python_libraries_used'] = 'pandas, numpys, matplotlib, seaborn'


dir = 'C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The Bridge\Gina\TICS_SALUD_EDA'  
file_name = "info.json"

with open(dir, 'w+') as outfile:
    json.dump(file_name, outfile, indent=4)
    