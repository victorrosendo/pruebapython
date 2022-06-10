from numpy import random
import numpy as np
from numpy.lib.function_base import copy

arreglo= np.arange(100)
lista=[]
for i in range (100):
    x = random.randint(501)
    arreglo[i] = x
    
    
    if(i%2==0):
        
        lista.append(arreglo[i])


arreglo2=arreglo[:].copy()
for i in range (100):
    n=arreglo2[i]*3
    arreglo[i]=n
print(arreglo2)    
print(arreglo2.sum())
print(arreglo2.mean())




print(arreglo)    
print("Numero mayor: ",arreglo.max())    
print("Numeor menor: ",arreglo.min()) 
print(lista) 
hola=arreglo.max()
pos=np.where(arreglo==hola)
print(pos)