'''ECUACIÓN 2'''
import matplotlib.pyplot as plt
import math as ma

#Definir el método de Euler con Taylor
def euler(f, x, y, h, n):
    u = []
    v = []
    for i in range(n):
        x = x + h
        y = y + h * f(x, y)
        u.append(x)
        v.append(y)
    return u, v

# Definir la EDO
def f(x, y):
    return 2*x*ma.exp(-3*x)-3*y


#azul
x1 = 0
y1 = 1
h1 = 0.1
n1 = 20
u1, v1 = euler(f, x1, y1, h1, n1)

#naranja
x2 = -0.7
y2 = 0
h2 = 0.1
n2 = 45
u2, v2 = euler(f, x2, y2, h2, n2)


# Graficar la solución
plt.plot(u1, v1)
plt.plot(u2, v2)
plt.grid(True)
plt.show()