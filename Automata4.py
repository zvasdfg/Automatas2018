import colorama
import sys
sys.setrecursionlimit(2000)

#Definicion del Diccionario
automata={
      (1,'0'):1,
      (1,'1'):1,
      (1,'2'):1,
      (1,'3'):1,
      (1,'4'):1,
      (1,'5'):1,
      (1,'6'):1,
      (1,'7'):1,
      (1,'8'):1,
      (1,'9'):1,
      (1,'A'):1,
      (1,'B'):1,
      (1,'C'):1,
      (1,'D'):1,
      (1,'E'):15,
      (1,'F'):1,
      (1,'G'):1,
      (1,'H'):1,
      (1,'I'):1,
      (1,'J'):1,
      (1,'K'):1,
      (1,'L'):1,
      (1,'M'):1,
      (1,'N'):1,
      (1,'O'):1,
      (1,'P'):1,
      (1,'Q'):1,
      (1,'R'):1,
      (1,'S'):1,
      (1,'T'):1,
      (1,'U'):1,
      (1,'V'):1,
      (1,'W'):12,
      (1,'X'):1,
      (1,'Y'):1,
      (1,'Z'):1,
      (1,'Ñ'):1,
      (1,'.'):1,
      (1,':'):1,
      (1,','):1,
      (1,';'):1,
      (1,'\n'):1,
      (1,'\r'):1,
      (1,'\t'):1,

##################################################
      (12,'0'):1,
      (12,'1'):1,
      (12,'2'):1,
      (12,'3'):1,
      (12,'4'):1,
      (12,'5'):1,
      (12,'6'):1,
      (12,'7'):1,
      (12,'8'):1,
      (12,'9'):1,
      (12,'A'):1,
      (12,'B'):1,
      (12,'C'):1,
      (12,'D'):1,
      (12,'E'):135,
      (12,'F'):1,
      (12,'G'):1,
      (12,'H'):1,
      (12,'I'):1,
      (12,'J'):1,
      (12,'K'):1,
      (12,'L'):1,
      (12,'M'):1,
      (12,'N'):1,
      (12,'O'):1,
      (12,'P'):1,
      (12,'Q'):1,
      (12,'R'):1,
      (12,'S'):1,
      (12,'T'):1,
      (12,'U'):1,
      (12,'V'):1,
      (12,'W'):12,
      (12,'X'):1,
      (12,'Y'):1,
      (12,'Z'):1,
      (12,'Ñ'):1,
      (12,'.'):1,
      (12,':'):1,
      (12,','):1,
      (12,';'):1,
      (12,'\n'):1,
      (12,'\r'):1,
      (12,'\t'):1,

##################################################
      (135,'0'):1,
      (135,'1'):1,
      (135,'2'):1,
      (135,'3'):1,
      (135,'4'):1,
      (135,'5'):1,
      (135,'6'):1,
      (135,'7'):1,
      (135,'8'):1,
      (135,'9'):1,
      (135,'A'):1,
      (135,'B'):146,
      (135,'C'):1,
      (135,'D'):1,
      (135,'E'):15,
      (135,'F'):1,
      (135,'G'):1,
      (135,'H'):1,
      (135,'I'):1,
      (135,'J'):1,
      (135,'K'):1,
      (135,'L'):1,
      (135,'M'):1,
      (135,'N'):1,
      (135,'O'):1,
      (135,'P'):1,
      (135,'Q'):1,
      (135,'R'):1,
      (135,'S'):1,
      (135,'T'):1,
      (135,'U'):1,
      (135,'V'):1,
      (135,'W'):12,
      (135,'X'):1,
      (135,'Y'):1,
      (135,'Z'):1,
      (135,'Ñ'):1,
      (135,'.'):1,
      (135,':'):1,
      (135,','):1,
      (135,';'):1,
      (135,'\n'):1,
      (135,'\r'):1,
      (135,'\t'):1,

##################################################
      (146,'0'):1,
      (146,'1'):1,
      (146,'2'):1,
      (146,'3'):1,
      (146,'4'):1,
      (146,'5'):1,
      (146,'6'):1,
      (146,'7'):1,
      (146,'8'):1,
      (146,'9'):1,
      (146,'A'):17,
      (146,'B'):1,
      (146,'C'):1,
      (146,'D'):1,
      (146,'E'):15,
      (146,'F'):1,
      (146,'G'):1,
      (146,'H'):1,
      (146,'I'):1,
      (146,'J'):1,
      (146,'K'):1,
      (146,'L'):1,
      (146,'M'):1,
      (146,'N'):1,
      (146,'O'):1,
      (146,'P'):1,
      (146,'Q'):1,
      (146,'R'):1,
      (146,'S'):1,
      (146,'T'):1,
      (146,'U'):1,
      (146,'V'):1,
      (146,'W'):12,
      (146,'X'):1,
      (146,'Y'):1,
      (146,'Z'):1,
      (146,'Ñ'):1,
      (146,'.'):1,
      (146,':'):1,
      (146,','):1,
      (146,';'):1,
      (146,'\n'):1,
      (146,'\r'):1,
      (146,'\t'):1,

##################################################
      (15,'0'):1,
      (15,'1'):1,
      (15,'2'):1,
      (15,'3'):1,
      (15,'4'):1,
      (15,'5'):1,
      (15,'6'):1,
      (15,'7'):1,
      (15,'8'):1,
      (15,'9'):1,
      (15,'A'):1,
      (15,'B'):16,
      (15,'C'):1,
      (15,'D'):1,
      (15,'E'):15,
      (15,'F'):1,
      (15,'G'):1,
      (15,'H'):1,
      (15,'I'):1,
      (15,'J'):1,
      (15,'K'):1,
      (15,'L'):1,
      (15,'M'):1,
      (15,'N'):1,
      (15,'O'):1,
      (15,'P'):1,
      (15,'Q'):1,
      (15,'R'):1,
      (15,'S'):1,
      (15,'T'):1,
      (15,'U'):1,
      (15,'V'):1,
      (15,'W'):1,
      (15,'X'):1,
      (15,'Y'):1,
      (15,'Z'):1,
      (15,'Ñ'):1,
      (15,'.'):1,
      (15,':'):1,
      (15,','):1,
      (15,';'):1,
      (15,'\n'):1,
      (15,'\r'):1,
      (15,'\t'):1,

##################################################
      (16,'0'):1,
      (16,'1'):1,
      (16,'2'):1,
      (16,'3'):1,
      (16,'4'):1,
      (16,'5'):1,
      (16,'6'):1,
      (16,'7'):1,
      (16,'8'):1,
      (16,'9'):1,
      (16,'A'):17,
      (16,'B'):1,
      (16,'C'):1,
      (16,'D'):1,
      (16,'E'):15,
      (16,'F'):1,
      (16,'G'):1,
      (16,'H'):1,
      (16,'I'):1,
      (16,'J'):1,
      (16,'K'):1,
      (16,'L'):1,
      (16,'M'):1,
      (16,'N'):1,
      (16,'O'):1,
      (16,'P'):1,
      (16,'Q'):1,
      (16,'R'):1,
      (16,'S'):1,
      (16,'T'):1,
      (16,'U'):1,
      (16,'V'):1,
      (16,'W'):12,
      (16,'X'):1,
      (16,'Y'):1,
      (16,'Z'):1,
      (16,'Ñ'):1,
      (16,'.'):1,
      (16,':'):1,
      (16,','):1,
      (16,';'):1,
      (16,'\n'):1,
      (16,'\r'):1,
      (16,'\t'):1,

##################################################
      (17,'0'):1,
      (17,'1'):1,
      (17,'2'):1,
      (17,'3'):1,
      (17,'4'):1,
      (17,'5'):1,
      (17,'6'):1,
      (17,'7'):1,
      (17,'8'):1,
      (17,'9'):1,
      (17,'A'):1,
      (17,'B'):1,
      (17,'C'):1,
      (17,'D'):1,
      (17,'E'):15,
      (17,'F'):1,
      (17,'G'):1,
      (17,'H'):1,
      (17,'I'):1,
      (17,'J'):1,
      (17,'K'):1,
      (17,'L'):1,
      (17,'M'):1,
      (17,'N'):1,
      (17,'O'):1,
      (17,'P'):1,
      (17,'Q'):1,
      (17,'R'):1,
      (17,'S'):1,
      (17,'T'):1,
      (17,'U'):1,
      (17,'V'):1,
      (17,'W'):1,
      (17,'X'):12,
      (17,'Y'):18,
      (17,'Z'):1,
      (17,'Ñ'):1,
      (17,'.'):1,
      (17,':'):1,
      (17,','):1,
      (17,';'):1,
      (17,'\n'):1,
      (17,'\r'):1,
      (17,'\t'):1,

##################################################
      (18,'0'):1,
      (18,'1'):1,
      (18,'2'):1,
      (18,'3'):1,
      (18,'4'):1,
      (18,'5'):1,
      (18,'6'):1,
      (18,'7'):1,
      (18,'8'):1,
      (18,'9'):1,
      (18,'A'):1,
      (18,'B'):1,
      (18,'C'):1,
      (18,'D'):1,
      (18,'E'):15,
      (18,'F'):1,
      (18,'G'):1,
      (18,'H'):1,
      (18,'I'):1,
      (18,'J'):1,
      (18,'K'):1,
      (18,'L'):1,
      (18,'M'):1,
      (18,'N'):1,
      (18,'O'):1,
      (18,'P'):1,
      (18,'Q'):1,
      (18,'R'):1,
      (18,'S'):1,
      (18,'T'):1,
      (18,'U'):1,
      (18,'V'):1,
      (18,'W'):12,
      (18,'X'):1,
      (18,'Y'):1,
      (18,'Z'):1,
      (18,'Ñ'):1,
      (18,'.'):1,
      (18,':'):1,
      (18,','):1,
      (18,';'):1,
      (18,'\n'):1,
      (18,'\r'):1,
      (18,'\t'):1,

       }

      
aceptacion=[18]  #estado de aceptacion
def ebay(string, current, automata, aceptacion,TEbay):#creamos la funcion
    if string == "":#cuando no encuentra nada
        print("Tokens Ebay: ", TEbay)
        return current in aceptacion #retorna true

    else:
        letter= string[0] # comienza con el primer caracter
        if(current,letter)in automata: # compara (estado,letra) se encuentra en automata
            destination=automata[(current,letter)]#si es asi destination tendra el nuevo valor estado
            #print(destination,"-->")
            remaining_string=string[1:]#comenzara a recorrer los demas caracteres
            if(current == 18):
                TEbay = TEbay + 1
            return ebay(remaining_string,destination,automata,aceptacion,TEbay)#funcion recursiva

        else:
            print (string)
            print (current)
            print (letter)
            return #si no es asi retorna falso


aceptacion=[146]  #estado de aceptacion
def web(string, current, automata, aceptacion,TWeb):#creamos la funcion
    if string == "":#cuando no encuentra nada
        print("Tokens Web: ", TWeb)
        return current in aceptacion #retorna true

    else:
        letter= string[0] # comienza con el primer caracter
        if(current,letter)in automata: # compara (estado,letra) se encuentra en automata
            destination=automata[(current,letter)]#si es asi destination tendra el nuevo valor estado
            #print(destination,"-->")
            remaining_string=string[1:]#comenzara a recorrer los demas caracteres
            if(current == 146):
                TWeb = TWeb + 1
            return web(remaining_string,destination,automata,aceptacion,TWeb)#funcion recursiva

        else:
            print (string)
            print (current)
            print (letter)
            return #si no es asi retorna falso

#hacemos una prueba

archivo = open ("Ejemplo.txt", "r")
cadena = archivo.read()
archivo.close()
ebay(cadena.upper().replace(' ','').replace('\t',''),1,automata,aceptacion,0)
web(cadena.upper().replace(' ','').replace('\t',''),1,automata,aceptacion,0)