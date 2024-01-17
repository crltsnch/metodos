import matplotlib.pyplot as plt
from math import e
import numpy as np


#Definir el método de Euler con Taylor
def true_solution1(x):
    return (x**2)/(e**(x**2))


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
    return (2*x/(1-x**2))*v-((m*(m+1))/(1-x**2))*u


def error(v, v_aprox):
    return abs(v - v_aprox)


x_inicial = 0
x_final = 0.95
x = 0
u = 0
v = 1
n = 100
h = (x_final - x_inicial)/n
m = 1
r0, t0 = euler2(f, x, u, v, h, n, m)



#Graficas las tres soluciones exactas
#x_exacta1 = np.linspace(x, x+n*h, n)
#y_exacta1 = true_solution1(x_exacta1)


# Graficar la solución
plt.plot(r0, t0)
#plt.plot(u1, v1, x_exacta1, y_exacta1)
#definir el intervalo de x en la que quiero que el grafico se mueva 0, 1.5
plt.grid(True)
plt.show()