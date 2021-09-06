import matplotlib.pyplot as plt
from numpy import exp


Valores = [[0, 1, 0, 1],
           [0, 0, 1, 1]]

Y = [1, 0, 0, 1]

W = [0.2, -0.5, 0.6, 0.9, 0.03, 0.01]
fi = 0
h = [0, 0]
Yp = 0
alpha = 0.25
C = []
iteraciones = []
f = 0
E = 0
#while E > 0.0000005:
for f in range(5000):
    #f += 1
    print("Generacion " + str(f) +':')
    for i in range(4):

        fi = W[0]*Valores[0][int(i)] + W[1]*Valores[1][int(i)]
        h[0] = 1 / (1 + exp(-fi))

        fi = W[2]*Valores[0][int(i)] + W[3]*Valores[1][int(i)]
        h[1] = 1 / (1 + exp(-fi))

        fi = W[4]*h[0] + W[5]*h[1]
        Yp = 1 / (1 + exp(-fi))

        W[5] = W[5] + alpha*h[1]*Yp*(1-Yp)*(Y[int(i)] - Yp)
        W[4] = W[4] + alpha*h[0]*Yp*(1-Yp)*(Y[int(i)] - Yp)

        W[3] = W[3] + alpha * \
            Valores[1][int(i)]*h[1]*(1-h[1]) * \
            (W[5] * h[1]*Yp*(1-Yp)*(Y[int(i)] - Yp))

        W[2] = W[2] + alpha * \
            Valores[0][int(i)]*h[1]*(1-h[1]) * \
            (W[5] * h[1]*Yp*(1-Yp)*(Y[int(i)] - Yp))


        W[1] = W[1] + alpha * \
            Valores[1][int(i)]*h[0]*(1-h[0]) * \
            (W[4] * h[0]*Yp*(1-Yp)*(Y[int(i)] - Yp))

        W[0] = W[0] + alpha * \
            Valores[0][int(i)]*h[0]*(1-h[0]) * \
            (W[4] * h[0]*Yp*(1-Yp)*(Y[int(i)] - Yp))

        print(Yp)
        E = pow((Yp - Y[int(i)]), 2)/2
        C.append(E)
        iteraciones.append(4*f+i+1)

#print(W)
plt.plot(iteraciones, C, 'r--')
plt.xlabel('Iteración')
plt.ylabel('C')