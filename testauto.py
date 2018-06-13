from random import randint
 
n = int(input("Ingrese N\n"))
m = int(input("Ingrese M\n"))
matriz = []
 
for i in range(n):
    matriz.append([ randint(0, 100) for i in range(m)])
        
print (matriz)