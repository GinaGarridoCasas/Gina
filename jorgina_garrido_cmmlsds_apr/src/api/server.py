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
        ENS_201_agr_json = read_json("Gina\\jorgina_garrido_cmmlsds_apr\\data\\Bases_trabajo\\ENS_2017_C_agr.json")
        return str(ENS_201_agr_json)
    else:
        return "No es la contraseña correcta"

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x", type=str, help="Password")
    arg = vars(parser.parse_args())
    if arg['x'] == "8642":
            app.run(host='127.0.0.1',port=os.getenv("PORT", 6060), debug=True)
    else:
        print('wrong password')




    