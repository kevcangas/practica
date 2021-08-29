# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:38:21 2021

@author: ROXANA
"""

import numpy as np
import math

def fx(x): #Función x a derivar
    a = (x+10) * (x+10) 
    return a

def fy(y): #Función y a derivar
    a = 0
    return a

def der_x(x,y,h): #Derivada
    a = (fx(x+h) - fx(x-h))/(2*h)
    b = (fy(y+h) - fy(y-h))/(2*h)
    return a,b

def m_gradiente(dim, iteraciones, alpha, xi, yi, h): #Método numerico
    
    for i in range(iteraciones):
        a,b = der_x(xi,yi,h)
        xi = xi - alpha*a
        yi = yi - alpha*b
        
    return xi,yi

x = -8
y = 0
h = 0.01
i = 100
a = 0.1
dim = 2

d = m_gradiente(dim, i, a, x, y, h)

print(d)