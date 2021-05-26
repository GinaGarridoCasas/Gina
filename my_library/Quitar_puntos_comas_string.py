# Quitar las comas

TICS_2017['Declaran acceso_internet_2017'] = TICS_2017['Declaran acceso_internet_2017'].apply(lambda x: x.split(',')).apply(''.join)

# Quitar los puntos
    
TICS_2017['Declaran acceso_internet_2017'] = TICS_2017['Declaran acceso_internet_2017'].apply(lambda x: x.split('.')).apply(''.join)

# Una vez cambiado ya se puede pasar con astype el strint a integer o float    
        