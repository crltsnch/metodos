'''ECUACIÓN 1'''

import matplotlib.pyplot as plt
from math import e
import numpy as np


#Definir el método de Euler con Taylor
def true_solution1(x):
    return (x**2)/(e**(x**2))

def true_solution2(x):
    return ((x**2)+1)/(e**(x**2))

def true_solution3(x):
    return ((x**2)-1)/(e**(x**2))


def euler(f, x, y, h, n):
    u = []
    v = []
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        u.append(x)
        v.append(y)
    return u, v

# Definir la EDO
def f(x, y):
    return -2*x*y + (2*x/(e**(x**2)))

def error(v, v_aprox):
    return abs(v - v_aprox)


x1 = 0
y1 = 0
h = 0.2
n = 20
u1, v1 = euler(f, x1, y1, h, n)

x2 = 0
y2 = 1
h = 0.2
n = 20
u2, v2 = euler(f, x2, y2, h, n)

x3 = 0
y3 = -1
h = 0.2
n = 20
u3, v3 = euler(f, x3, y3, h, n)


#Graficas las tres soluciones exactas
x_exacta1 = np.linspace(x1, x1+n*h, n)
x_exacta2 = np.linspace(x2, x2+n*h, n)
x_exacta3 = np.linspace(x3, x3+n*h, n)
y_exacta1 = true_solution1(x_exacta1)
y_exacta2 = true_solution2(x_exacta2)
y_exacta3 = true_solution3(x_exacta3)


# Graficar la solución
plt.plot(u1, v1, u2, v2, u3, v3, x_exacta1, y_exacta1, x_exacta2, y_exacta2, x_exacta3, y_exacta3)
#definir el intervalo de x en la que quiero que el grafico se mueva 0, 1.5
plt.axis([0, 1.5, -1.5, 1.5])
plt.grid(True)
#plt.show()


#Valor real, valor aproximado y error
v = true_solution1(1.5)
print('Valor real: ', v)
v_aprox = v1[-1]
print('Valor aproximado: ', v_aprox)
print('Error: ', error(v, v_aprox))