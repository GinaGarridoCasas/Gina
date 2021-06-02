import json
import os

data = {}
data['nombre_proyecto'] = '¿Son más saludables en España las poblaciones con mejores conexiones a TICS?'
data['autora'] = 'Jorgina Garrido Casas'
data['linkedin'] = ''
data['mail'] = 'jorginagc@gmail.com'
data['Título_proyecto'] = '¿Son más saludables las poblaciones con mejores conexiones a TICS?'
data['Descripción_proyecto'] = 'e identifican las correlaciones entre diferentes tipos de conexión de banda ancha y diferentes determinantes de salud física y mental en España'
data['flask_port'] = '6060'
data['streamlit_port'] = ''
data['python_libraries_used'] = 'pandas, numpys, matplotlib, seaborn' 


dir = 'C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The Bridge\Gina\TICS_SALUD_EDA'  
file_name = "info.json"

with open(dir, 'w+') as outfile:
    json.dump(file_name, outfile, indent=4)

  