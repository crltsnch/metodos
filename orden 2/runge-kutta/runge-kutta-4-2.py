import matplotlib.pyplot as plt
import numpy as np
import math 


def runge_kutta_4_2(f, x, u, v, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver una EDO de orden 2
    '''
    r = []
    t = []
    for i in range(n):
        k11 = v
        k12 = f(x, u, v)
        k21 = v + (h/2) * k12
        k22 = f(x + (h/2), u + ((h/2) * k11), v + ((h/2) * k12))
        k31 = v + ((h/2) * k22)
        k32 = f(x + (h/2), u + ((h/2) * k21), v + ((h/2) * k22))
        k41 = v + (h * k32)
        k42 = f(x + h, u + (h * k31), v + (h * k32))

        x = x + h
        u = u + (h/6) * (k11 + (2 * k21) + (2 * k31) + k41)
        v = v + (h/6) * (k12 + (2 * k22) + (2 * k32) + k42)
        r.append(x)
        t.append(u)
    return r, t

def f(x, u, v):
    '''
    Aquí se define la EDO de orden 2
    '''
    return (x*v - u*2)/(0.999 - x*2)


# DATOS
# -----
# Rango de x
x_inicial = -1
x_final = 1
# Datos iniciales
x = -0.999
u = -1 # Recodar que la u es la y
v =  2 # Es y'
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 100
h = (x_final - x_inicial)/n

# Aplicamos el método de Runge-Kutta de orden 4 para resolver la EDO de segundo orden
r, t = runge_kutta_4_2(f, x, u, v, h, n)


# Graficar la solución
# --------------------
plt.plot(r, t, label='Solución numérica')
plt.xlabel('x')
plt.ylabel('u(x)')

plt.legend()
plt.grid(True)
plt.show()