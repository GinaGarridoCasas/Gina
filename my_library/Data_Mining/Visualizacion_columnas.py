# boxplot

plt.figure(figsize=(15,8))

boxplot = TICS_Salud.boxplot(column=['Tasa_paro', 'Indice_masculinidad', 'Edad_25_59 años', 'Educacion_superior'])
boxplot.plot()

plt.savefig("../reports/Outliers/Control.jpg", bbox_inches='tight')


# tendencias

TICS_Salud['Declaran acceso_internet_2017'].plot()
plt.savefig("../reports/Tendencias/Acceso_internet.jpg", bbox_inches='tight')

# Histogramas
plt.hist(x=TICS_Salud['ADSL'], bins=5, color='#F2AB6D', rwidth=0.85)
plt.title('Hogares con conexión ADSL')
plt.xlabel('ADSL(%)')
plt.ylabel('Frecuencia')

plt.savefig("../reports/Histograma/ADSL_.jpg", bbox_inches='tight')