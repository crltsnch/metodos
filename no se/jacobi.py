import matplotlib.pyplot as plt
import numpy as np
import math

def runge_kutta_4_2(f, x, u, v, alfa, beta, h, n):
    r = []
    t = []
    for i in range(n):
        k11 = v
        k12 = f(x, u, v, alfa, beta)
        k21 = v + (h/2) * k12
        k22 = f(x + (h/2), u + ((h/2) * k11), v + ((h/2) * k12), alfa, beta)
        k31 = v + ((h/2) * k22)
        k32 = f(x + (h/2), u + ((h/2) * k21), v + ((h/2) * k22), alfa, beta)
        k41 = v + (h * k32)
        k42 = f(x + h, u + (h * k31), v + (h * k32), alfa, beta)

        x = x + h
        u = u + (h/6) * (k11 + (2 * k21) + (2 * k31) + k41)
        v = v + (h/6) * (k12 + (2 * k22) + (2 * k32) + k42)
        r.append(x)
        t.append(u)
    return r, t

def f(x, u, v, alfa, beta):
    return (x*v - u*(alfa + beta + 1))/(2 + (alfa + beta + 1)*x)

def polinomios(x, n, alfa, beta):
    return (-1)**n * math.factorial(n + beta) / (math.factorial(n)* math.factorial(beta + 1))

def derivada_pol(x, n, alfa, beta):
    if n == 0:
        return 0  # Manejar el caso especial cuando n es 0
    elif n == 1:
        return 1 / (beta + 1)
    else:
        return (-1)**n * (math.factorial(n + beta) / (math.factorial(n - 1) * math.factorial(beta + 1))) * (1 + n + alfa + beta)

# DATOS
# Constante alfa
alfa = float(input("Introduzca el valor de alfa: "))
# Constante beta
beta = float(input("Introduzca el valor de beta: "))

# Rango de x
x_inicial = -1
x_final = 1

# Número de subintervalos que nos permite calcular el valor de h (paso)
m = 100

for n in range(5):
    p = polinomios(x_inicial, n, alfa, beta)  # Recuerda que u es la y
    r = derivada_pol(x_inicial, n, alfa, beta)  # Es y'
    h = (x_final - x_inicial) / m

    # Aplicamos el método de Runge-Kutta de orden 4 para resolver la EDO de segundo orden
    x_vals, y_vals = runge_kutta_4_2(f, x_inicial, p, r, alfa, beta, h, m)

    plt.plot(x_vals, y_vals, label=f'Polinomio de Jacobi n={n}')

plt.xlabel('x')
plt.ylabel('u(x)')
plt.legend()
plt.grid(True)
plt.show()

