from flask import Flask, request, render_template
import pandas as pd
import os, sys
import json
import argparse

def read_json(fullpath):
    with open(fullpath, "r", encoding = 'utf-8') as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

app = Flask(__name__)  # __name__ --> __main__  

@app.route("/")  
def home():
    """ Default path """
   
    return "Bienvenidos a la API de Gina"

# localhost:6060/obtener_json?token_id=H13297422
@app.route('/obtener_json', methods=['GET'])
def give_id():
    x = request.args.get('token_id')
    if x == "H13297422":
        Base_completa_json = read_json("C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The Bridge\Gina\TICS_SALUD_EDA\src\api\static\Base_completa.json")
        return Base_completa_json
    else:
        return "No es la contraseña correcta"

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x", type=str, help="Password")
    arg = parser.recoger_argumentos()
    if arg['x'] == "8642":
            app.run(host='0.0.0.0',port=os.getenv("PORT", 6060), debug=True)
    else:
        print('wrong password')




    