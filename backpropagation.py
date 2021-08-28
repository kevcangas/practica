

import numpy as np
import math


def entrenamiento(pesosIniciales, entradas, salidaDeseada, salidaReal, alpha):
    
    iteracionesI = len(entradas)
    iteracionesJ = len(salidaReal)

    pesosNuevos = []
    error = []
    

    for j in range(iteracionesJ):
        error.append(salidaReal[j] * (1 - salidaReal[j]) * (salidaDeseada[j] - salidaReal[j]))
        
        for i in range(iteracionesI):
            pesosNuevos.append(pesosIniciales[i]+alpha*entradas[i]*error[j])

    return pesosNuevos,error

def f_activacion(entradas,pesos):
    a = len(entradas)
    salida = 0

    for i in range(a):
        salida = salida + entradas[i] * pesos[i]
    
    salida = 1/(1+math.exp(-salida))
    
    return salida

#Entradas
ent1 = [0.343,0.574]
ent2 = [0,1]
ent3 = [1,0]
ent4 = [1,1]

entradas = np.array([ent1,ent2,ent3,ent4])

#Configuración
pesosIniciales = [0.2,0.4]
alpha = 0.1

#Salidas deseadas
sal1 = [1]
sal2 = [0]
sal3 = [0]
sal4 = [1]

salidas = np.array([sal1,sal2,sal3,sal4])

#Entrenamiento
for i in range(1):
    
    for j in range (1):
        
        salidaReal = [f_activacion(entradas[j],pesosIniciales)]
        pesosIniciales,error = entrenamiento(pesosIniciales, entradas[j], salidas[j], salidaReal, alpha)

print(error)
print(pesosIniciales)

print(f_activacion(ent1,pesosIniciales))
print(f_activacion(ent2,pesosIniciales))
print(f_activacion(ent3,pesosIniciales))
print(f_activacion(ent4,pesosIniciales))