import matplotlib.pyplot as plt
import numpy as np
import math

def funcionX(x, u, v):
    return -v + u * (1 - u**2 - v**2)

def funcionY(x, u, v):
    return u + v * (1 - u**2 - v**2)

def runge_kutta_sistemas(funcionX, funcionY, x, y1, y2, h, n):
    r1 = []
    u1 = []
    v1 = []
    for i in range(n):
        k11 = funcionX(x, y1, y2)
        k12 = funcionY(x, y1, y2)
        k21 = funcionX(x + (h/2), y1 + ((h/2) * k11), y2 + ((h/2) * k12))
        k22 = funcionY(x + (h/2), y1 + ((h/2) * k11), y2 + ((h/2) * k12))
        k31 = funcionX(x + (h/2), y1 + ((h/2) * k21), y2 + ((h/2) * k22))
        k32 = funcionY(x + (h/2), y1 + ((h/2) * k21), y2 + ((h/2) * k22))
        k41 = funcionX(x+h, y1+(h*k31), y2+(h*k32))
        k42 = funcionY(x+h, y1+(h*k31), y2+(h*k32))

        x = x+h
        y1 = y1 + (k11+2*k21+2*k31+k41)*h/6
        y2 = y2 + (k12+2*k22+2*k32+k42)*h/6
        r1.append(x)
        u1.append(y1)
        v1.append(y2)
    return r1, u1, v1

def generar_datos_iniciales(num_conjuntos):
    datos_iniciales = []
    for _ in range(num_conjuntos):
        u_inicial = np.random.uniform(-2, 2)
        v_inicial = np.random.uniform(-2, 2)
        datos_iniciales.append((u_inicial, v_inicial))
    return datos_iniciales

def graficar_plano_fases(datos_iniciales, n):
    for u_inicial, v_inicial in datos_iniciales:
        x = 0
        y1 = u_inicial
        y2 = v_inicial
        h = 20/n
        r1, u1, v1 = runge_kutta_sistemas(funcionX, funcionY, x, y1, y2, h, n)
        plt.plot(u1, v1)

    plt.xlabel('u')
    plt.ylabel('v')
    plt.legend()
    plt.grid(True)
    plt.show()

# DATOS
# -----
# Rango de x
x_inicial = 0
x_final = 20
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 400

# Generar datos iniciales aleatorios
num_conjuntos = 15
datos_iniciales = generar_datos_iniciales(num_conjuntos)

# Graficar el plano de fases con los datos iniciales
graficar_plano_fases(datos_iniciales, n)
