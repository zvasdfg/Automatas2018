automata={                 #usamos mapas o diccionarios
      (1,'0'):2,
      (1,'1'):2,
      (1,'2'):2,
      (1,'3'):2,
      (1,'4'):2,
      (1,'5'):2,
      (1,'6'):2,
      (1,'7'):2,
      (1,'8'):2,
      (1,'9'):2,
      (1,'-'):8,
      (1,'+'):8,
      (1,'.'):8,
      (1,'E'):8,

      (2,'0'):2,
      (2,'1'):2,
      (2,'2'):2,
      (2,'3'):2,
      (2,'4'):2,
      (2,'5'):2,
      (2,'6'):2,
      (2,'7'):2,
      (2,'8'):2,
      (2,'9'):2,
      (2,'.'):3,
      (2,'E'):5,
      (2,'+'):8,
      (2,'-'):8,

      (3,'0'):4,
      (3,'1'):4,
      (3,'2'):4,
      (3,'3'):4,
      (3,'4'):4,
      (3,'5'):4,
      (3,'6'):4,
      (3,'7'):4,
      (3,'8'):4,
      (3,'9'):4,
      (3,'-'):8,
      (3,'+'):8,
      (3,'.'):8,
      (3,'E'):8,

      (4,'0'):4,
      (4,'1'):4,
      (4,'2'):4,
      (4,'3'):4,
      (4,'4'):4,
      (4,'5'):4,
      (4,'6'):4,
      (4,'7'):4,
      (4,'8'):4,
      (4,'9'):4,
      (4,'E'):5,
      (4,'.'):8,
      (4,'-'):8,
      (4,'+'):8,

      (5,'0'):7,
      (5,'1'):7,
      (5,'2'):7,
      (5,'3'):7,
      (5,'4'):7,
      (5,'5'):7,
      (5,'6'):7,
      (5,'7'):7,
      (5,'8'):7,
      (5,'9'):7,
      (5,'+'):6,
      (5,'-'):6,
      (5,'.'):8,
      (5,'E'):8,

      (6,'0'):7,
      (6,'1'):7,
      (6,'2'):7,
      (6,'3'):7,
      (6,'4'):7,
      (6,'5'):7,
      (6,'6'):7,
      (6,'7'):7,
      (6,'8'):7,
      (6,'9'):7,
      (6,'+'):8,
      (6,'-'):8,
      (6,'.'):8,
      (6,'E'):8,

      (7,'0'):7,
      (7,'1'):7,
      (7,'2'):7,
      (7,'3'):7,
      (7,'4'):7,
      (7,'5'):7,
      (7,'6'):7,
      (7,'7'):7,
      (7,'8'):7,
      (7,'9'):7,
      (7,'+'):8,
      (7,'-'):8,
      (7,'.'):8,
      (7,'E'):8,

      (8,'0'):8,
      (8,'1'):8,
      (8,'2'):8,
      (8,'3'):8,
      (8,'4'):8,
      (8,'5'):8,
      (8,'6'):8,
      (8,'7'):8,
      (8,'8'):8,
      (8,'9'):8,
      (8,'+'):8,
      (8,'-'):8,
      (8,'.'):8,
      (8,'E'):8,
       }
aceptacion=[7,4]  #estado de aceptacion
def recon(string, current, automata, aceptacion):#creamos la funcion
    if string == "":#cuando no encuentra nada
        return current #retorna true
    else:
        letter= string[0] # comienza con el primer caracter
        if(current,letter)in automata: # compara (estado,letra) se encuentra en automata
            destination=automata[(current,letter)]#si es asi destination tendra el nuevo valor estado
            print(destination,"-->")
            if destination == 8:
                return 
            else:
                remaining_string=string[1:]#comenzara a recorrer los demas caracteres
                return recon(remaining_string,destination,automata,aceptacion)#funcion recursiva
        else:
            print(destination, "-->")
            return current #si no es asi retorna falso
#hacemos una prueba
cadena = input("Ingrese una cadena para reconocer si es un numero real\n en notacion decimal o Exponencial: ")
valor = (recon(cadena.upper(),1,automata,aceptacion))
print(valor)
if valor == 2:
    print("ERROR : \nNumero Entero sin decimal :  ", cadena.upper())
elif valor == 3:
    print("ERROR : \nNo hay numeros despues del punto Decimal : ", cadena.upper())
elif valor == 4:
    print("CORRECTO : \nEs un Numero Real con Punto Decimal", cadena.upper())
elif valor == 5:
    print("ERROR : \nNo hay nada despues de el simbolo 'E' de Exponente", cadena.upper())
elif valor == 6:
    print("ERROR : \nNo hay nada despues de el simbolo '+/-'", cadena.upper())
elif valor == 7:
    print("CORRECTO : \nEs un Numero Real con Notacion Exponencial\n", cadena.upper())
elif valor == 8:
    print("ERROR : \nError de escritura", cadena.upper())
