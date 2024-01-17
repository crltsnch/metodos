import matplotlib.pyplot as plt
import numpy as np
import math 


def runge_kutta_4_sistemas(f1, f2, t, x, y, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver sistemas de EDOs de primer orden
    '''
    r = []
    u = []
    v = []
    for i in range(n):
        k11 = f1(t, x, y)
        k12 = f2(t, x, y)
        k21 = f1(t + (h/2), x + ((h/2) * k11), y + ((h/2) * k12))
        k22 = f2(t + (h/2), x + ((h/2) * k11), y + ((h/2) * k12))
        k31 = f1(t + (h/2), x + ((h/2) * k21), y + ((h/2) * k22))
        k32 = f2(t + (h/2), x + ((h/2) * k21), y + ((h/2) * k22))
        k41 = f1(t + h, x + (h * k31), y + (h * k32))
        k42 = f2(t + h, x + (h * k31), y + (h * k32))

        t = t + h
        x = x + (h/6) * (k11 + (2 * k21) + (2 * k31) + k41)
        y = y + (h/6) * (k12 + (2 * k22) + (2 * k32) + k42)
        r.append(t)
        u.append(x)
        v.append(y)
    return r, u, v

def f1(t, x, y):
    '''
    Aquí se define la primera EDO de orden 1 del sistema
    '''
    return 3*x - x*y #p*x-q*x*y

def f2(t, x, y):
    '''
    Aquí se define la segunda EDO de orden 1 del sistema
    '''
    return -2*y + x*y  #-r*y+s*x*y

# DATOS
# -----
# Rango de t (tiempo)
t_inicial = 0 # Normalmente siempre arranca en 0
t_final = 5
# Datos iniciales
t = 0
x = 10 # Primera EDO1 del sistema
y = 5 # Segunda EDO1 del sistema

# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 100
h = (t_final - t_inicial)/n

# Aplicamos el método de Runge-Kutta de orden 4 para resolver el sistema de EDOs de primer orden
r, u, v = runge_kutta_4_sistemas(f1, f2, t, x, y, h, n)


# Graficar la solución
# --------------------
plt.plot(r, u, label='Solución EDO x(t)')
plt.plot(r, v, label='Solución EDO y(t)')
plt.xlabel('x')

plt.legend()
plt.grid(True)
plt.show()