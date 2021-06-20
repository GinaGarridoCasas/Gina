# leer ficheros csv
TICS_Salud = pd.read_csv("../data/Bases/Base_completa.csv", sep =',')


# archivar dataset a csv
Base_completa.to_csv('../data/Bases/Base_completa.csv')


# archivar dataset a json
Base_completa.to_json("../src/api/static/Base_completa.json", orient = "records", force_ascii= False)