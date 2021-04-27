a = "armadillo"
letra = "a"

# Número de veces que aparece una letra en una palabra

def f1y(x,y):
    import f1x
    n_veces = 0
    for i in x:
        if i == y:
            n_veces +=1
                                    
    return n_veces
        
        
f1y(a, letra) 

# añadir una letra a una palabra

a = "armadillo"
b = "s"

def f1y(x,y):
    import f2x
    z= x + y                
    return z
            
print(f1y(a,b))