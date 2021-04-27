
import os
import sys

ruta = __file__ 
print(ruta)
for i in range(3):
	ruta = os.path.dirname(ruta)

sys.path.append(ruta)

import imports.a.x as xpy

	
a= ["1","2"]
b=["23", "34"]

def f1y():
    print ('f1y' )
    xpy.f1x()
    

def f2y():  # DA ERROR, LLAMARÁ TAMBIÉN A LA FUNCIÓN f2z QUE A SU VEZ LLAMA A f2x
    print('f2y') 
    xpy.f2x



	



    