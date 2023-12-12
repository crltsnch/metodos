import matplotlib.pyplot as plt
import numpy as np
import math 


p = float(input("Introduzca el valor de p: "))
q = float(input("Introduzca el valor de q: "))
r = float(input("Introduzca el valor de r: "))
s = float(input("Introduzca el valor de s: "))

def funcionX(x, u, v):
    return p*u-q*u*v

def funcionY(x, u, v):
    return -r*v+s*u*v

def runge_kutta_sistemas(funcionX, funcionY, x, y1, y2, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver una EDO de orden 2
    '''
    r1 = []
    u1 = []
    v1 = []
    for i in range(n):
        k11 = funcionX(x, y1, y2)
        k12 = funcionY(x, y1, y2)
        k21 = funcionX(x + (h/2), y1 + ((h/2) * k11), y2+((h/2)*k12))
        k22 = funcionY(x + (h/2), y1 + ((h/2) * k11), y2+((h/2)*k12))
        k31 = funcionX(x + (h/2), y1 + ((h/2) * k21), y2+((h/2)*k22))
        k32 = funcionY(x + (h/2), y1 + ((h/2) * k21), y2+((h/2)*k22))
        k41 = funcionX(x+h, y1+(h*k31), y2+(h*k32))
        k42 = funcionY(x+h, y1+(h*k31), y2+(h*k32))

        x = x+h
        y1 = y1 + (k11+2*k21+2*k31+k41)*h/6
        y2 = y2 + (k12+2*k22+2*k32+k42)*h/6
        r1.append(x)
        u1.append(y1)
        v1.append(y2)
    return r1, u1, v1




# DATOS
# -----
# Rango de x
x_inicial = 0
x_final = 5
# Datos iniciales
x = 0
y1 = 10 # Recodar que la u es la y
y2 =  5 # Es y'
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 100
h = (x_final - x_inicial)/n

# Aplicamos el método de Runge-Kutta de orden 4 para resolver la EDO de segundo orden
r1, u1, v1 = runge_kutta_sistemas(funcionX, funcionY, x, y1, y2, h, n)


# Graficar la solución
# --------------------
plt.plot(r1, u1, label='Solución numérica x(t)')
plt.plot(r1, v1, label='Solución numérica y(t)')
plt.xlabel('x')

plt.legend()
plt.grid(True)
plt.show()