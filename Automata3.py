num_estados = int(input('Ingrese numero de estados: '))
num_trans = int(input('Ingrese numero de transiciones: '))


Estados = []
Transiciones = []

for i in range(num_estados):
    if(i == 0):
        print('Introduce estado inicial: ')
        Estados.append(input())
    else:
        print('Introduce estado :')  
        Estados.append(input())
for i in range(num_trans):
    print('Introduce  Transicion:')    
    Transiciones.append(input())  

print(Estados)
print(Transiciones)

filas = num_estados
columnas = num_trans

tabla = [[0 for x in range(num_trans)] for y in range(num_estados)] 

for i in range(num_trans):
    tabla[i][0] = Transiciones[i] 

for i in range(num_estados):
    tabla[0][i] = Estados[i]             
print(tabla)

