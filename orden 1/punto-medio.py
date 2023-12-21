# MÉTODO DE RUNGE-KUTTA -- ORDEN 2

import matplotlib.pyplot as plt
from math import e

def true_solucion(x):
    return (x**2)*e**(-x**2)

def taylor(f, x, y, h, n):
    '''
    Función que implementa el método de Taylor para resolver una EDO
    '''
    u = []
    v = []
    for i in range(n):
        y = y + h * f(x + (h/2), y + (h/2)*f(x, y)) 
        x = x + h
        u.append(x)
        v.append(y)
    return u, v

def f(x, y):
    '''
    Aquí se define la EDO
    '''
    return 2*x*(e**(-x**2)-y)


def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)


# DATOS
x_inicial = 0
x_final = 1.5
x = 0# Esto se modifica
y = 0  # Esto se modifica
n = 10 
h = (x_final - x_inicial)/n

# Aplicamos el método de Euler
u, v = taylor(f, x, y, h, n)

# Imprimimos la última y del bucle
print('w_100: ', v[-1])
print("Solucion real: ", true_solucion(1.5))

# Error
print('Error: ', error(true_solucion(1.5), v[-1]))

# Graficar la solución
plt.plot(u, v)
plt.grid(True)
#plt.show()