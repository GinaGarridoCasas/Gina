# valores absolutos
freq = ENS_2017_1['IMCa'].value_counts() 

# Valores relativos
freq_R = ENS_2017_1['IMCa'].value_counts() / len(ENS_2017_1['IMCa'])*100

# Suma de frecuencias
freq.sum()
