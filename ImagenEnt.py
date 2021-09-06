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

def entrenamiento(pesosIniciales, entradas, salidaDeseada, salidaReal,\
    alpha, conexion, error, pesoConexion):
    
    iteracionesI = len(entradas)
    pesosNuevos = []

    for i in range(len(entradas)):
        pesosNuevos.append(0)

    if(conexion == 0):
        error = salidaReal * (1 - salidaReal) * (salidaDeseada - salidaReal)
        
    else:
        error = salidaReal * (1 - salidaReal) * (pesoConexion  * error) 
    
    for i in range(iteracionesI):
        pesosNuevos[i] = pesosIniciales[i]+alpha*entradas[i]*error

    return pesosNuevos,error

def f_activacion(entradas,pesos):
    a = len(entradas)
    salida = 0

    for i in range(a):
        salida = salida + entradas[i] * pesos[i]
    
    salida = 1/(1+math.exp(-salida))
    
    return salida

#Configuración
went = []
for i in range(16):
    went.append(rand(35))

wneu = []
for i in range(4):
    wneu.append(rand(4))


alpha = 0.25

#Salidas deseadas
salidas = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1]\
    ,[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1]\
    ,[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1]\
    ,[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]

dif1 = 1
dif2 = 1
dif3 = 1
dif4 = 1

gen = 0

#Entrenamiento
#for i in range(5000):
while dif1 > 0.0005 or dif2 > 0.0005 or dif3 > 0.0005 or dif4 > 0.0005:
    for j in range(16):

        #Bloque 1

        ne1 = f_activacion(entradas[j],went[0])
        ne2 = f_activacion(entradas[j],went[1])
        ne3 = f_activacion(entradas[j],went[2])
        ne4 = f_activacion(entradas[j],went[3])

        no = f_activacion([ne1,ne2,ne3,ne4],wneu[0])

        wneu[0],error = entrenamiento(wneu[0], [ne1,ne2,ne3,ne4], salidas[j][3], no, alpha, 0, 0, 0)
        
        went[0],a = entrenamiento(went[0], entradas[j], 0, ne1, alpha, 1, error, wneu[0][0])
        went[1],b = entrenamiento(went[1], entradas[j], 0, ne2, alpha, 1, error, wneu[0][1])
        went[2],b = entrenamiento(went[2], entradas[j], 0, ne3, alpha, 1, error, wneu[0][2])
        went[3],b = entrenamiento(went[3], entradas[j], 0, ne4, alpha, 1, error, wneu[0][3]) 

        dif1 = 1/2*(no - salidas[j][3])*(no - salidas[j][3])

        #Bloque 2

        ne5 = f_activacion(entradas[j],went[4])
        ne6 = f_activacion(entradas[j],went[5])
        ne7 = f_activacion(entradas[j],went[6])
        ne8 = f_activacion(entradas[j],went[7])

        no1 = f_activacion([ne5,ne6,ne7,ne8],wneu[1])

        wneu[1],error1 = entrenamiento(wneu[1], [ne5,ne6,ne7,ne8], salidas[j][2], no1, alpha, 0, 0, 0)
        
        went[4],a = entrenamiento(went[4], entradas[j], 0, ne5, alpha, 1, error1, wneu[1][0])
        went[5],b = entrenamiento(went[5], entradas[j], 0, ne6, alpha, 1, error1, wneu[1][1])
        went[6],b = entrenamiento(went[6], entradas[j], 0, ne7, alpha, 1, error1, wneu[1][2])
        went[7],b = entrenamiento(went[7], entradas[j], 0, ne8, alpha, 1, error1, wneu[1][3]) 

        dif2 = 1/2*(no1 - salidas[j][2])*(no1 - salidas[j][2])

       #Bloque 3

        ne9 = f_activacion(entradas[j],went[8])
        ne10 = f_activacion(entradas[j],went[9])
        ne11 = f_activacion(entradas[j],went[10])
        ne12 = f_activacion(entradas[j],went[11])

        no2 = f_activacion([ne9,ne10,ne11,ne12],wneu[2])

        wneu[2],error2 = entrenamiento(wneu[2], [ne9,ne10,ne11,ne12], salidas[j][1], no2, alpha, 0, 0, 0)
        
        went[8],a = entrenamiento(went[8], entradas[j], 0, ne9, alpha, 1, error2, wneu[2][0])
        went[9],b = entrenamiento(went[9], entradas[j], 0, ne10, alpha, 1, error2, wneu[2][1])
        went[10],b = entrenamiento(went[10], entradas[j], 0, ne11, alpha, 1, error2, wneu[2][2])
        went[11],b = entrenamiento(went[11], entradas[j], 0, ne12, alpha, 1, error2, wneu[2][3]) 

        dif3 = 1/2*(no2 - salidas[j][1])*(no2 - salidas[j][1])

        #Bloque 4

        ne13 = f_activacion(entradas[j],went[12])
        ne14 = f_activacion(entradas[j],went[13])
        ne15 = f_activacion(entradas[j],went[14])
        ne16 = f_activacion(entradas[j],went[15])

        no3 = f_activacion([ne13,ne14,ne15,ne16],wneu[3])

        wneu[3],error3 = entrenamiento(wneu[3], [ne13,ne14,ne15,ne16], salidas[j][0], no3, alpha, 0, 0, 0)
        
        went[12],a = entrenamiento(went[12], entradas[j], 0, ne13, alpha, 1, error3, wneu[3][0])
        went[13],b = entrenamiento(went[13], entradas[j], 0, ne14, alpha, 1, error3, wneu[3][1])
        went[14],b = entrenamiento(went[14], entradas[j], 0, ne15, alpha, 1, error3, wneu[3][2])
        went[15],b = entrenamiento(went[15], entradas[j], 0, ne16, alpha, 1, error3, wneu[3][3])  

        dif4 = 1/2*(no3 - salidas[j][0])*(no3 - salidas[j][0])

        gen = gen + 1
        print("Generación: " + str(gen) + "\n")



archivo = open("pesosE.txt","w")
for i in range(len(went)):
    archivo.write(str(went[i]) + "\n")
archivo.close()

archivo = open("pesosN.txt","w")
for i in range(len(wneu)):
    archivo.write(str(wneu[i]) + "\n")
archivo.close()

print("Entrenamiento terminado")

"""""
#B1
a = f_activacion(entradas[0],went[0])
b = f_activacion(entradas[0],went[1])
c = f_activacion(entradas[0],went[2])
d = f_activacion(entradas[0],went[3])
ent = [a,b,c,d]

c = f_activacion(ent,wneu[0])
print(c)

#B2
a = f_activacion(entradas[1],went[4])
b = f_activacion(entradas[1],went[5])
c = f_activacion(entradas[1],went[6])
d = f_activacion(entradas[1],went[7])
ent = [a,b,c,d]

c = f_activacion(ent,wneu[1])
print(c)

#B3
a = f_activacion(entradas[0],went[8])
b = f_activacion(entradas[0],went[9])
c = f_activacion(entradas[0],went[10])
d = f_activacion(entradas[0],went[11])
ent = [a,b,c,d]

c = f_activacion(ent,wneu[2])
print(c)

#B4
a = f_activacion(entradas[0],went[12])
b = f_activacion(entradas[0],went[13])
c = f_activacion(entradas[0],went[14])
d = f_activacion(entradas[0],went[15])
ent = [a,b,c,d]

c = f_activacion(ent,wneu[3])
print(c)
"""

