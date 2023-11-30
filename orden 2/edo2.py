'''Hacemos un cambio de variables:
u = y ;  v = y'
Entonces: u' = v  ;  v' = - av - bu + f
Con esto queremos conseguir una ecucion de primer orden. Ponemos la ecuacion y los datos iniciales como vectores.'''

import matplotlib.pyplot as plt
from math import e
import numpy as np


#Definir el método de Euler con Taylor
'''def true_solution1(x):
    return (x**2)/(e**(x**2))'''


def euler2(f, x, u, v, h, n, m):  #m es la ecuacion de bessel
    r = []
    t = []
    for i in range(n):   
        x = x + h
        u = u + h * v
        v = v + h * f(x, u, v, m)
        r.append(x)
        t.append(u) 
    return r, t

# Definir la EDO
def f(x, u, v, m):
    return (-1/x)*v-(1-((m**2)/x**2))*u


def error(v, v_aprox):
    return abs(v - v_aprox)


x_inicial = 0.1
x_final = 20
x = 0.1
u = 0
v = 1
n = 1000
h = (x_final - x_inicial)/n
m = 0
r0, t0 = euler2(f, x, u, v, h, n, m)


x_inicial1 = 0.1
x_final1 = 20
x1 = 0.1
u1 = 1
v1 = 0
n1 = 1000
h1 = (x_final1 - x_inicial1)/n1
m1 = 0
r1, t1 = euler2(f, x1, u1, v1, h1, n1, m1)

#Graficas las tres soluciones exactas
#x_exacta1 = np.linspace(x, x+n*h, n)
#y_exacta1 = true_solution1(x_exacta1)


# Graficar la solución
plt.plot(r0, t0, r1, t1)
#plt.plot(u1, v1, x_exacta1, y_exacta1)
#definir el intervalo de x en la que quiero que el grafico se mueva 0, 1.5
plt.grid(True)
plt.show()


#Valor real, valor aproximado y error
'''v = true_solution1(1.5)
print('Valor real: ', v)
v_aprox = v1[-1]
print('Valor aproximado: ', v_aprox)
print('Error: ', error(v, v_aprox))'''