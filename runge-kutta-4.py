# MÉTODO DE RUNGE-KUTTA -- ORDEN 4

import matplotlib.pyplot as plt


def taylor(f, x, y, h, n):
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
    return (1 + 4*x*y)/(3*x**2)


def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)


# DATOS
x = 0.5
y = -1
h = 0.035
n = 100

# Aplicamos el método de Euler
u, v = taylor(f, x, y, h, n)

# Imprimimos la última y del bucle
print('w_100: ', v[-1])

# Error
v_e = -11.46
print('Error: ', error(v_e, v[-1]))

# Graficar la solución
plt.plot(u, v)
plt.grid(True)
#plt.show()