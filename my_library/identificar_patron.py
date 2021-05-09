import re


    def patron():
        #comprueba que tenga el formato adecuado.
        
        casilla = input ('Teclea la casila elegida: ')
        patron= r'^[1-9]|10[vh][1-9]|10:[1-9]|10$'
    
        