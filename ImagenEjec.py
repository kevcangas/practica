import numpy as np
import math
from numpy.random import rand

#Entradas
A = [0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0\
    ,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0]

B = [0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0\
    ,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0]

C = [0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0\
    ,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0]

D = [0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0\
    ,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0]

E = [0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0\
    ,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0]

F = [0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0\
    ,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]

A0 = [0,1,1,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0\
     ,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0]

A1 = [0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0\
     ,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0] 

A2 = [0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0\
     ,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0]

A3 = [0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0\
     ,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0]

A4 = [0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0\
     ,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0]

A5 = [0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0\
     ,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0]

A6 = [0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0\
     ,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0]

A7 = [0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0\
     ,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0]

A8 = [0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0\
     ,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0]

A9 = [0,1,1,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0\
     ,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0]

entradas = np.array([A,B,C,D,E,F,A0,A1,A2,A3,A4,A5,A6,A7,A8,A9])

def f_activacion(entradas,pesos):
    a = len(entradas)
    salida = 0

    for i in range(a):
        salida = salida + entradas[i] * pesos[i]
    
    salida = 1/(1+math.exp(-salida))
    
    return salida

#Obtención de pesos del archivo
went = []
wneu = []
aux = []

archivo = open("pesosE.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    x = linea.split(",")
    for i in range(len(x)):
        
        if '[' in x[i]:
            x[i] = x[i].replace('[', ' ')
        
        elif ']' in x[i]:
            x[i] = x[i].replace(']', ' ')

        aux.append(float(x[i]))
    
    went.append(aux)
    aux = []
archivo.close()

archivo = open("pesosN.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    x = linea.split(",")
    for i in range(len(x)):
        
        if '[' in x[i]:
            x[i] = x[i].replace('[', ' ')
        
        elif ']' in x[i]:
            x[i] = x[i].replace(']', ' ')

        aux.append(float(x[i]))
    wneu.append(aux)
    aux = []
archivo.close()

z = 0
comp = [0,0,0,0]

#B1
a = f_activacion(entradas[z],went[0])
b = f_activacion(entradas[z],went[1])
c = f_activacion(entradas[z],went[2])
d = f_activacion(entradas[z],went[3])
ent = [a,b,c,d]

e = f_activacion(ent,wneu[0])
print(e)

if e < 0.5 :
    comp[3] = 0
else:
    comp[3] = 1

#B2
a = f_activacion(entradas[z],went[4])
b = f_activacion(entradas[z],went[5])
c = f_activacion(entradas[z],went[6])
d = f_activacion(entradas[z],went[7])
ent = [a,b,c,d]

e = f_activacion(ent,wneu[1])
print(e)

if e < 0.5 :
    comp[2] = 0
else:
    comp[2] = 1


#B3
a = f_activacion(entradas[z],went[8])
b = f_activacion(entradas[z],went[9])
c = f_activacion(entradas[z],went[10])
d = f_activacion(entradas[z],went[11])
ent = [a,b,c,d]

e = f_activacion(ent,wneu[2])
print(e)

if e < 0.5 :
    comp[1] = 0
else:
    comp[1] = 1


#B4
a = f_activacion(entradas[z],went[12])
b = f_activacion(entradas[z],went[13])
c = f_activacion(entradas[z],went[14])
d = f_activacion(entradas[z],went[15])
ent = [a,b,c,d]

e = f_activacion(ent,wneu[3])
print(e)

if e < 0.5 :
    comp[0] = 0
else:
    comp[0] = 1

#Switch para impresión de la letra
if comp == [0,0,0,0]:
    print("A")

elif comp == [0,0,0,1]:
    print("B")

elif comp == [0,0,1,0]:
    print("C")

elif comp == [0,0,1,1]:
    print("D")

elif comp == [0,1,0,0]:
    print("E")

elif comp == [0,1,0,1]:
    print("F")

elif comp == [0,1,1,0]:
    print("0")

elif comp == [0,1,1,1]:
    print("1")

elif comp == [1,0,0,0]:
    print("2")

elif comp == [1,0,0,1]:
    print("3")

elif comp == [1,0,1,0]:
    print("4")

elif comp == [1,0,1,1]:
    print("5")

elif comp == [1,1,0,0]:
    print("6")

elif comp == [1,1,0,1]:
    print("7")

elif comp == [1,1,1,0]:
    print("8")

elif comp == [1,1,1,1]:
    print("9")
