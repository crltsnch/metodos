# MÉTODO DE RUNGE-KUTTA -- ORDEN 2

import matplotlib.pyplot as plt


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