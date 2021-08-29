import numpy as np
import math

def ferror(entradas,pesos,salidaDeseada): #Derivada
    a = (1/2)*(f_activacion(entradas,pesos)-salidaDeseada)**2
    return a

def der_x(h,entradas,pesos,salidaDeseada): #Derivada
    pesosa=[0,0]
    pesosb=[0,0]

    pesosa[0] = pesos[0]+h
    pesosa[1] = pesos[1]+h
    pesosb[0] = pesos[0]-h
    pesosb[1] = pesos[1]-h
    
    a = (ferror(entradas,pesosa,salidaDeseada) - ferror(entradas,pesosb,salidaDeseada))/(2*h)
    return a

def entrenamiento(pesosIniciales, entradas, salidaDeseada, salidaReal,\
    alpha, conexion, error, pesoConexion):
    
    iteracionesI = len(entradas)
    pesosNuevos = [0,0]

    if(conexion == 0):
        error = der_x(0.1,entradas,pesosIniciales,salidaDeseada)
        
    else:
        error = salidaReal * (1 - salidaReal) * (pesoConexion * error)
    
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

#Entradas
ent1 = [0,0]
ent2 = [0,1]
ent3 = [1,0]
ent4 = [1,1]

entradas = np.array([ent1,ent2,ent3,ent4])

#Configuración
w1 = [0.1,-0.7]
w2 = [0.5,0.3]
w3 = [0.2,0.4]
alpha = 0.25

#Salidas deseadas
sal1 = 0
sal2 = 0
sal3 = 0
sal4 = 1

salidas = np.array([sal1,sal2,sal3,sal4])

#Entrenamiento
for i in range(5000):
    
    for j in range (4):

        ne1 = f_activacion(entradas[j],w1)
        ne2 = f_activacion(entradas[j],w2)

        no = f_activacion([ne1,ne2],w3)

        w3c = w3

        w3,error = entrenamiento(w3, [ne1,ne2], salidas[j], no, alpha, 0, 0, 0)
        
        w1,a = entrenamiento(w1, entradas[j], 0, ne1, alpha, 1, error, w3c[0])
        w2,b = entrenamiento(w2, entradas[j], 0, ne2, alpha, 1, error, w3c[1])
        
        

a = f_activacion(entradas[0],w1)
b = f_activacion(entradas[0],w2)
ent = [a,b]

c = f_activacion(ent,w3)
print(c)

a = f_activacion(entradas[1],w1)
b = f_activacion(entradas[1],w2)
ent = [a,b]

c = f_activacion(ent,w3)
print(c)

a = f_activacion(entradas[2],w1)
b = f_activacion(entradas[2],w2)
ent = [a,b]

c = f_activacion(ent,w3)
print(c)

a = f_activacion(entradas[3],w1)
b = f_activacion(entradas[3],w2)
ent = [a,b]

c = f_activacion(ent,w3)
print(c)