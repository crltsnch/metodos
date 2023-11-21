# MÉTODO DE RUNGE-KUTTA -- ORDEN 4

import matplotlib.pyplot as plt
from math import e

def true_solucion(x):
    return (x + 1)**2 - (e**x)/2

def rungekutta4(f, x, y, h, n):
    '''
    Función que implementa el método de Runge-Kutta para resolver una EDO
    '''
    u = []
    v = []
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + (h/2), y + (h/2)*k1)
        k3 = f(x + (h/2), y + (h/2)*k2)
        k4 = f(x + h, y + h*k3)
        a1 = 1/6
        a2 = 1/3
        a3 = 1/3
        a4 = 1/6
        x = x + h
        y = y + h * (a1*k1 + a2*k2 + a3*k3 + a4*k4)
        u.append(x)
        v.append(y)
    return u, v

def f(x, y):
    '''
    Aquí se define la EDO
    '''
    return y-x**2+1


def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)


# DATOS
x = 0
y = 1/2  
h = 0.1 
n = 5

# Aplicamos el método de Euler
u, v = rungekutta4(f, x, y, h, n)

# Solución real y solución del método
solucion_metodo = round(v[-1], 7)
print('w_100: ', solucion_metodo)
solucion_real = round(true_solucion(1/2), 7)
print('Solucion real: ', solucion_real)

# Error
error = error(solucion_real, v[-1])

print('Error: ', round(error, 7))

# Graficar la solución
plt.plot(u, v)
plt.grid(True)
#plt.show()