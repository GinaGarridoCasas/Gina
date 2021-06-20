# Quitar las comas

TICS_2017['Declaran acceso_internet_2017'] = TICS_2017['Declaran acceso_internet_2017'].apply(lambda x: x.split(',')).apply(''.join)

# Quitar los puntos
    
TICS_2017['Declaran acceso_internet_2017'] = TICS_2017['Declaran acceso_internet_2017'].apply(lambda x: x.split('.')).apply(''.join)

# Una vez cambiado ya se puede pasar con astype el strint a integer o float

TICS_2017[['ADSL', 'cable_fibra optica','otras conexiones', 'conexion movil_dispositivo_mano', 'movil_USB']]= TICS_2017[['ADSL', 'cable_fibra optica','otras conexiones', 'conexion movil_dispositivo_mano', 'movil_USB']].astype(float)


# Reemplazar la coma por un punto de una variable string para poder pasarla a float

TICS_2017 = TICS_2017.stack().str.replace(',','.').unstack()    
        