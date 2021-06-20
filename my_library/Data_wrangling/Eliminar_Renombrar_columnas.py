# Eliminar columnas 

TO_TICS_2017 = ['Viviendas con conexión de banda ancha', 'Viviendas con conexión de banda estrecha', 'Conexión de banda estrecha por llamada telefónica a través de su línea de teléfono convencional (módem) o RDSI','Conexión móvil de banda estrecha (otros teléfonos móviles -GPRS-)']
TICS_2017.drop(TO_TICS_2017, inplace = True, axis=1)

# Eliminar columna index del dataset (Concentrarse)
del Concentrarse['index']

# Renombrar columnas

TICS_2017 = TICS_2017.rename(columns = 
{'Total de viviendas que disponen de acceso a Internet y declaran las formas de conexión utilizadas': 'Declaran acceso_internet_2017', 
'Conexión de banda ancha por ADSL': 'ADSL', 
'Conexión de banda ancha por red de cable o fibra óptica': 'cable_fibra optica',
'Otras conexiones fijas de banda ancha (vía satélite, WiFi público o WiMax)': 'otras conexiones', 
'Conexión móvil de banda ancha vía modem USB ó tarjeta (en portátiles, p.ej.)':'movil_USB'})

# Renombrar la columna 4
TICS_2017.rename(columns={ TICS_2017.columns[5]: 'conexion movil_dispositivo_mano' }, inplace = True)


# Renombramos algunas categorías de la columna

TICS_2017["index"] = TICS_2017["index"].replace({"Asturias. Principado de":"Asturias, Principado de" , "Balears. Illes":"Balears, Illes", "Madrid. Comunidad de": "Madrid, Comunidad de", "Murcia. Región de":"Murcia, Región de","Navarra. Comunidad Foral de": "Navarra, Comunidad Foral de", "Rioja. La": "Rioja, La"})