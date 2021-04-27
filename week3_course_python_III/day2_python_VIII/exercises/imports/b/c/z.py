import os
import sys

ruta = __file__ 
print(ruta)
for i in range(4):
	ruta = os.path.dirname(ruta)

sys.path.append(ruta)

import imports.a.x as xpy
import imports.b.y as ypy
	

a= [1,2,3,4]
b=[23, 34, 56, 67]

def f1z():
    print ('f1z' )
    ypy.f1y()

def f2z():
    print('f2z')
    xpy.f2x()

f1z()