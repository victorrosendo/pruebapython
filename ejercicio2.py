import numpy as np
from numpy import random

arreglo_1 = np.arange(10)
cantidad = 0
total = 0

for n in range(10):
    num = random.randint(0,1001)
    arreglo_1[n] = num

#Mostrar el arreglo
print(arreglo_1)

#contar los elementos pares
for i in range(10):
    if(arreglo_1[i]%2 == 0):
        cantidad = cantidad + 1

print(f"Cantidad de elementos pares {cantidad}")

#suma de elementos impares
for x in range(10):
    if(arreglo_1[x]%2 != 0):
        total = total + arreglo_1[x]

print(f"La suma de los impares es {total}")

#Mostrar numeros primos
for i in range(10):
    contador = 0
    for n in range(1,arreglo_1[i]+1):
        if(arreglo_1[i]% n == 0):
            contador = contador + 1

    if(contador == 2):
        print(f"El numero {arreglo_1[i]} es primo")
    


