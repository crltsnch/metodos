'''ECUACIÓN 1'''

import matplotlib.pyplot as plt
from math import e

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
    return (e**x)/((1+e**x)*y)


#azul
x1 = -2
y1 = 1
h1 = 0.04
n1 = 100
u1, v1 = euler(f, x1, y1, h1, n1)
#imprime la ultima y del bucle
print(v1[-1])

# Graficar la solución

'''plt.plot(u1, v1)
plt.grid(True)
plt.show()'''