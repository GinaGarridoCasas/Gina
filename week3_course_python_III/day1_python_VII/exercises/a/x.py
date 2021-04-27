a = [1,2,3]
b= [23, 24, 25]


#suma de dos listas
def f1x(x,y):
    suma = []
    for i, w in enumerate (x):
        suma.append (x[i]+y[i]) 
    return suma

#elevar a una potencia los valores de una lista
n= 4
def f2x(x):
    exp3 =[]
    for i in x:
        exp3.append(i**n)
    return exp3
    
print(f2x(a))
    





    
